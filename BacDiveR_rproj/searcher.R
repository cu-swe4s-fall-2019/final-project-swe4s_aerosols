# Library Prep
if(!require('devtools')) install.packages('devtools'); devtools::install_github('TIBHannover/BacDiveR')
library(BacDiveR)
library(magrittr)
library(ggplot2)
library(tidyr)
library(readr)
library(tidyverse)
library(attempt)


# Create data frames
tax_table <- read_csv('tax_table.csv')
tax_table$Genus <- gsub('_', ' ', tax_table$Genus)
tax_table$Species <- gsub('_', ' ', tax_table$Species)

tax_table$Genus <- gsub('-', '', tax_table$Genus)
tax_table$Species <- gsub('-', '', tax_table$Species)

tax_table$Genus <- gsub(' ', '', tax_table$Genus)
tax_table$Species <- gsub(' ', '', tax_table$Species)

tax_table$Genus <- gsub('/', '', tax_table$Genus)
tax_table$Species <- gsub('/', '', tax_table$Species)

#Create new fields for spore and temp
tax_table_annot <- tax_table
tax_table_annot$spore <- NA
tax_table_annot$temp <- NA


# Define Functions to extract subfields we want
extract_temps <- function(dataset, taxon_name) {
  purrr::map(.x = dataset, .f = ~.x$culture_growth_condition$culture_temp$temp) %>% 
    unlist() %>%
    as.numeric() %>%
    data.frame(temp_C = ., taxon = rep(taxon_name, length(.))) %>%
    return()
}

extract_spore <- function(dataset, taxon_name) {
  purrr::map(.x = dataset, .f = ~.x$morphology_physiology$spore_formation$ability) %>% 
    unlist() %>%
    data.frame(spore_L = ., taxon = rep(taxon_name, length(.))) %>%
    return()
}

extract_gc <- function(dataset, taxon_name) {
  purrr::map(.x = dataset, .f = ~.x$molecular_biology$GC_content) %>% 
    unlist() %>%
    as.numeric() %>%
    data.frame(temp_C = ., taxon = rep(taxon_name, length(.))) %>%
    return()
}





# Loop through taxa, download data nrow(tax_uniq) for (i in 1:nrow(tax_table_annot))
for (i in 1:25) {
  
  if (!is.na(tax_table_annot$Species[i])) {
    taxa <- paste(tax_table_annot$Genus[i], tax_table_annot$Species[i])
  } else if (is.na(tax_table_annot$Species[i])) {
    taxa <- paste(tax_table_annot$Genus[i])
  }
  
  print(paste('Retrieving', taxa))
  
  tryCatch({
    Bac_data <- bd_retrieve_taxon(name = taxa)
  }, error=function(e){cat("ERROR :",conditionMessage(e), "\n")})
  temperature_Bac <- extract_temps(Bac_data, taxa)
  spore_Bac <- extract_spore(Bac_data, taxa)
  
  if (length(temperature_Bac$temp_C) == 0) {  # Add temperatures
    print(paste(taxa, "temp not found in BacDive"))
    next
  } else if (length(temperature_Bac$temp_C) > 0) {
    tax_table_annot$temp[i] <- mean(temperature_Bac$temp_C) # Assign average temperature value
    print(paste("Adding", temperature_Bac$temp_C))
    
  }
    
  if (length(spore_Bac$spore_L) > 0) {  # Add spore formation ability
    tax_table_annot$spore[i] <- spore_Bac[1,1]
    print(paste("Adding", spore_Bac$spore_L))}
      
}

write.csv(tax_table_annot, file = "tax_table_annot3.csv", row.names = FALSE)  












# Export Annotated Tax Table
write.csv(tax_table_annot, file = "tax_table_annot.csv", row.names = FALSE)
#Plot Example
tax_table_annot %>% 
  ggplot(aes(x = tax_table_annot$Genus, y = tax_table_annot$temp)) +
  geom_boxplot(notch = TRUE) +
  geom_jitter(height = 0, alpha = 0.5)
#> notch went outside hinges. Try setting notch=FALSE.






''' # UNUSED CODE



taxon_1 <- 'Collinsella aerofaciens'
Bac_data <- bd_retrieve_taxon(name = taxon_1)

taxon_2 <- tax_table$Genus[16]
At_data <- bd_retrieve_taxon(name = taxon_2)




temperature_Bac <- extract_temps(Bac_data, taxon_1) 
temperature_At <- extract_temps(At_data, taxon_2)

rbind(temperature_Bac, temperature_At) %>% 
  ggplot(aes(x = taxon, y = temp_C)) +
  geom_boxplot(notch = TRUE) +
  geom_jitter(height = 0, alpha = 0.5)
#> notch went outside hinges. Try setting notch=FALSE.


tax_uniq <- tax_table %>%
  as_tibble() %>%
distinct(Genus, Species, .keep_all = TRUE)

tax_uniq$Genus <- gsub('_', ' ', tax_uniq$Genus)
tax_uniq$Species <- gsub('_', ' ', tax_uniq$Species)


# Create BD Database
BDDB = c() #bac dive data base
for (i in 12:13) {
if (!is.na(tax_uniq$Species[i])) {
taxa <- paste(tax_table_annot$Genus[i], tax_table_annot$Species[i])
} else if (is.na(tax_table_annot$Species[i])) {
taxa <- paste(tax_table_annot$Genus[i])
}

Bac_data <- bd_retrieve_taxon(name = taxa)
BDDB <- append(BDDB, Bac_data)
}

saveRDS(BDDB, "BDDB.rds", version = 3)
BDDB_stored <- readRDS("BDDB.rds")
identical(BDDB, BDDB_stored)


'''