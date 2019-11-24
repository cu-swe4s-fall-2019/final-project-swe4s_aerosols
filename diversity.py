'''
This is a module that will take community data and calculate a variety of
diversity indices. First one is beta diversity, which is essentially a ratio
between regional and local diversity.
     - the most basic index of beta diversity is just S/A - 1, where S = total
     number of spp , and A is number of spp in the site (AKA true beta diversity)
     - in practice, most people use pairwise comparisons (i.e. comparisons between
     each pair of sites), so that diversity index isn't an artifact of sample size.

takes an input csv file with community data. each row should be a different
community, columns specify species. can be count data or binary
presence/absence.

'''
import sys
import csv
import argparse
import pandas as pd
import numpy as np

def betaDivtest1(file):
# extract total number of spp observed across all sites
   with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        #pull out spp names
        spp_names = None
        data = []
        communities = []
        number_spp_present = []
        for row in reader:
            if spp_names is None:
                spp_names = row
            else:
                communities.append(row.split()[0])
                spp_counts = row.split()[1:] #grab spp counts
                number_spp_present.append(length(spp_counts> 0))
        print(number_spp_present)

    #filename = file


def betaDiv(file):
    df = pd.read_csv(file, index_col = 0) #assumes first column is comm names
    num_spp = int(len(df.columns))
    counts = []
    for comm in range(num_spp):
        #print(comm)
        count = list(df.iloc[comm,:]>0).count(True)
        counts.append(count/num_spp)
    #print(counts)
    #bdiv = np.array(counts)/num_spp
    print(counts)
    #for row in df.iterrows():
    #beta = beta_diversity('observed beta', df, ids = list(df.index))


    #make a plot of beta div vs comm

    
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description = 'right way', prog = 'good way')

    parser.add_argument('--file_name', type=str, help='community data file', required = True)

    parser.add_argument('--diversitymeasure', type=str,
                    help='type of diversity: alpha, beta, dissimilarity',
                    required = False)

    args = parser.parse_args()

    if args.diversitymeasure == 'beta':
        betaDiv(str(args.file_name))

#python diversity.py --file_name test_community_dataset.csv --diversitymeasure beta
