# Aerobiology Toolkit

Microorganisms (bacteria, fungi, oomycota, etc.) are ubiquitous in the Earth's biosphere and influence global biogeochemical cycles, plant and animal disease, and possibly weather formation. The density and distribution of microorganisms in the atmosphere has been a recent focus of environmental microbiology research. To attempt to measure the diversity, quantity, and distribution of bacteria in the Earth's atmosphere, a C20-A jet, outfitted with an aerosol sampling instrument, was flown in the troposphere (0-10km) and lower stratosphere (12km)for the purpose of capturing microorganisms at altitude (Smith et al. 2018) https://doi.org/10.3389/fmicb.2018.01752.

Captured particulates on filters were DNA-extracted and sequenced with 16S amplicon sequencing. We used DADA2 (https://benjjneb.github.io/dada2/) to filter, denoise, and assign taxonomy to sequences. From the resulting amplicon sequence variants (ASVs)
We had 3 questions:
1. How does bacterial diversity change with altitude?
2. Are certain bacterial traits more common at high altitude?
3. How do individual bacteria genus/species quantities change with altitude?

# BacDive Phenotype Analysis
To query the BacDive (http://bacdive.dsmz.de/) database for each of our ~4600 ASVs, we used the BacDive WebTools through the BacDiveR package (https://github.com/TIBHannover/BacDiveR).

# Diversity analyses
To begin, we calculated diversity in a few different ways: first, we used beta diversity, which is often used in ecology to compare relative diversity of different communities that have some species in common. The advantage of this method is that it is both a relative term, but also allows comparison between very different communities and is a good measure of uniqueness. The module diversity.py calculates beta diversity using the asv table provided.
Next, we calculated species richness; the advantage of this metric is that it discounts abundance information, and instead is a measure of just how many unique species are in each community.
In order to characterize communities in more wholistic approach, we used ordination methods, which is a common approach in ecology to use with multivariate data. The goal is to compress multivariate data down to fewer axes while maintaining distinction between the groups of interest; in this case, we want to compare communities on a 2-D continuum, with axes that hopefully are representative of 'real' variation between communities. R package 'vegan' was used to accomplish this goal, and the module for computing and plotting NMDS results, along with species richness, are in 'nmds.R.'
We found that diversity changed insignificantly with altitude; the differences in diversity between altitudes were swamped by flight differences. This conclusion was reached using the NMDS approach; the two different diversity measures also showed no major differences between altitude groups. Thus, a possible avenue for future work is to try to better understand the difference between microbial communities in the air due to short-term wind patterns or other environmental variables. 
