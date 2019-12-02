#Install
if(!require('devtools')) install.packages('devtools'); devtools::install_github('TIBHannover/BacDiveR')

library(BacDiveR)
library(magrittr)
library(ggplot2)
taxon_1 <- "Dorea longicatena"
Bac_data <- bd_retrieve_taxon(name = taxon_1)

taxon_2 <- "Fusicatenibacter saccharivorans"
At_data <- bd_retrieve_taxon(name = taxon_2)

extract_temps <- function(dataset, taxon_name) {
  purrr::map(.x = dataset, .f = ~.x$culture_growth_condition$culture_temp$temp) %>% 
    unlist() %>%
    as.numeric() %>%
    data.frame(temp_C = ., taxon = rep(taxon_name, length(.))) %>%
    return()
}

extract_gc <- function(dataset, taxon_name) {
  purrr::map(.x = dataset, .f = ~.x$molecular_biology$GC_content) %>% 
    unlist() %>%
    as.numeric() %>%
    data.frame(gc_cont = ., taxon = rep(taxon_name, length(.))) %>%
    return()
}

gc_Bac <- extract_gc(Bac_data, taxon_1) 
gc_At <- extract_gc(At_data, taxon_2)

rbind(gc_Bac, gc_At) %>% 
  ggplot(aes(x = taxon, y = gc_cont)) +
  geom_boxplot(notch = TRUE) +
  geom_jitter(height = 0, alpha = 0.5)
#> notch went outside hinges. Try setting notch=FALSE.