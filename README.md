# Aerobiology Toolkit

Microorganisms (bacteria, fungi, oomycota, etc.) are ubiquitous in the Earth's biosphere and influence global biogeochemical cycles, plant and animal disease, and possibly weather formation. The density and distribution of microorganisms in the atmosphere has been a recent focus of environmental microbiology research. To attempt to measure the diversity, quantity, and distribution of bacteria in the Earth's atmosphere, a C20-A jet, outfitted with an aerosol sampling instrument, was flown in the troposphere (0-10km) and lower stratosphere (12km)for the purpose of capturing microorganisms at altitude (Smith et al. 2018) https://doi.org/10.3389/fmicb.2018.01752.

Captured particulates on filters were DNA-extracted and sequenced with 16S amplicon sequencing. We used DADA2 (https://benjjneb.github.io/dada2/) to filter, denoise, and assign taxonomy to sequences. From the resulting amplicon sequence variants (ASVs)
We had 3 questions:
1. How does bacterial diversity change with altitude?
2. Are certain bacterial traits more common at high altitude?
3. How do individual bacteria genus/species quantities change with altitude?

# BacDive Phenotype Analysis
To query the BacDive (http://bacdive.dsmz.de/) database for each of our ~4600 ASVs, we used the BacDive WebTools through the BacDiveR package (https://github.com/TIBHannover/BacDiveR). 
