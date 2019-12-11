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
import matplotlib.pyplot as plt


def betaDiv(file):
    df = pd.read_csv(file, index_col=0)  # assumes first column is comm names
    num_spp = int(len(df.columns))
    num_comms = int(len(df.index))
    counts = []
    for comm in range(num_comms):
        # print(comm)
        count = list(df.iloc[comm, :]>0).count(True)
        counts.append(count/num_spp)
    # print(counts)
    # bdiv = np.array(counts)/num_spp
    # print(counts)
    # print('len', len(counts))

    print(counts)
    # make a plot of beta div vs comm
    y_pos = np.arange(len(df.index))
    vals = np.array(counts)
    # print(y_pos)
    # print(vals)
    plt.bar(y_pos, vals, align = 'center')
    plt.xlabel('Community')
    plt.ylabel('Beta diversity')
    plt.title('Beta diversity score by community')
    plt.savefig('beta_diversity.png')

    return counts

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

# python diversity.py --file_name asv_table_corrected.csv --diversitymeasure beta
