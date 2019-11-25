#Install
if(!require('devtools')) install.packages('devtools'); devtools::install_github('TIBHannover/BacDiveR')

library(BacDiveR)
library(magrittr)
library(ggplot2)
taxon_1 <- "Bacillus halodurans"
Bac_data <- bd_retrieve_taxon(name = taxon_1)

taxon_2 <- "Aneurinibacillus thermoaerophilus"
At_data <- bd_retrieve_taxon(name = taxon_2)

extract_temps <- function(dataset, taxon_name) {
  purrr::map(.x = dataset, .f = ~.x$culture_growth_condition$culture_temp$temp) %>% 
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