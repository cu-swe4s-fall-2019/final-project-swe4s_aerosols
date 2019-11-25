library(BacDiveR)
library(magrittr)
library(ggplot2)
library(tidyr)
library(readr)

tax_table <- read_csv('tax_table.csv')

taxon_1 <- 'Bacillus subtilis'
Bac_data <- bd_retrieve_taxon(name = taxon_1)

taxon_2 <- tax_table$Genus[16]
Bac_data <- bd_retrieve_taxon(name = taxon_2)


extract_temps <- function(dataset, taxon_name) {
  purrr::map(.x = dataset, .f = ~.x$morphology_physiology$spore_formation$ability) %>% 
    unlist() %>%
    as.numeric() %>%
    data.frame(temp_C = ., taxon = rep(taxon_name, length(.))) %>%
    return()
}

temperature_Bac <- extract_temps(Bac_data, taxon_1) 
temperature_At <- extract_temps(At_data, taxon_2)

rbind(temperature_Bac, temperature_At) %>% 
  ggplot(aes(x = taxon, y = temp_C)) +
  geom_boxplot(notch = TRUE) +
  geom_jitter(height = 0, alpha = 0.5)
#> notch went outside hinges. Try setting notch=FALSE.