# A) Library Prep
if(!require('devtools')) install.packages('devtools'); devtools::install_github('TIBHannover/BacDiveR')
library(BacDiveR)
library(magrittr)
library(ggplot2)
library(tidyr)
library(readr)
library(tidyverse)
library(attempt)


# B) Function Definitions
extract_gc <- function(dataset, taxon_name) {
  purrr::map(.x = dataset, .f = ~.x$molecular_biology$GC_content) %>% 
    unlist() %>%
    as.numeric() %>%
    data.frame(gc_cont = ., taxon = rep(taxon_name, length(.))) %>%
    return()
}

extract_gram <- function(dataset, taxon_name) {
  purrr::map(.x = dataset, .f = ~.x$morphology_physiology$gram_stain) %>% 
    unlist() %>%
    as.numeric() %>%
    data.frame(gram = ., taxon = rep(taxon_name, length(.))) %>%
    return()
}

extract_spore <- function(dataset, taxon_name) {
  purrr::map(.x = dataset, .f = ~.x$morphology_physiology$spore_formation$ability) %>% 
    unlist() %>%
    data.frame(spore_L = ., taxon = rep(taxon_name, length(.))) %>%
    return()
}

extract_oxy <- function(dataset, taxon_name) {
  purrr::map(.x = dataset, .f = ~.x$morphology_physiology$oxygen_tolerance) %>% 
    unlist() %>%
    data.frame(oxy_L = ., taxon = rep(taxon_name, length(.))) %>%
    return()
}

# 1) Create Dataframes
tax_table <- read_csv('tax_table.csv')
tax_table$Genus <- gsub('_', ' ', tax_table$Genus)
tax_table$Species <- gsub('_', ' ', tax_table$Species)

tax_table$Genus <- gsub('-', '', tax_table$Genus)
tax_table$Species <- gsub('-', '', tax_table$Species)

tax_table$Genus <- gsub(' ', '', tax_table$Genus)
tax_table$Species <- gsub(' ', '', tax_table$Species)

tax_table$Genus <- gsub('/', '', tax_table$Genus)
tax_table$Species <- gsub('/', '', tax_table$Species)

tax_table_annot <- tax_table
tax_table_annot$spore <- NA
tax_table_annot$oxy <- NA


# 2: Pull BacDive Entry
## If Genus and Species are NOT NA, pull BacDive entries
for (i in 1:nrow(tax_table_annot)) {
  if (!is.na(tax_table_annot$Species[i])) {
    taxon <- paste(tax_table_annot$Genus[i], tax_table_annot$Species[i])
    tryCatch({
      Bac_lib <- bd_retrieve_taxon(name = taxon)
      print(paste('Retrieving', taxon))
    }, error=function(e){cat("ERROR :",conditionMessage(e), "\n")})
    ## Now that we have the BacDive entry, let's pull GC content and Spore (?)
    oxy_pull <- extract_oxy(Bac_lib, taxon)
    spore_pull <- extract_spore(Bac_lib, taxon)
    tryCatch({ # spore
      if (TRUE %in% spore_pull$spore_L) {
        tax_table_annot$spore[i] <- as.logical(TRUE)
        print(paste('Added', taxon, TRUE, ' spore to table'))
      }
      else {
        tax_table_annot$spore[i] <- as.logical(FALSE)
        print(paste('Added', taxon, FALSE, ' spore to table'))
      }
    }, error=function(e){cat("ERROR :", taxon, conditionMessage(e), "\n")})
    tryCatch({  # oxy
      if ('anaerobe' %in% oxy_pull$oxy_L) {
        tax_table_annot$oxy[i] <- 'anaerobe'
        print(paste('Added', taxon, 'anaerobe', ' to table'))
      } else if ('aerobe' %in% oxy_pull$oxy_L) {
        tax_table_annot$oxy[i] <- 'aerobe'
        print(paste('Added', taxon, 'aerobe', ' to table'))
      }
    }, error=function(e){cat("ERROR :", taxon, conditionMessage(e), "\n")})
    # Write CSV
    write.csv(tax_table_annot, file = "tax_table_oxy_spore.csv", row.names = FALSE)
  } else if (is.na(tax_table_annot$Species[i])) {
    next
  }
}











