import matplotlib as mp
import numpy as np
import csv
from numpy import genfromtxt
import sys
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt


def main():
    ground = []
    tropo = []
    strat = []
    anaer = []  # A list of ASVs that are anaerobic
    aer = []  # A list of ASVs that are aerobic
    spores = []  # A list of ASVs that form spores
    nospores = []  # A list of ASVs that do not form spores
    sample_ground = []  # A list to hold ground sample IDs
    sample_tropo = []  # A list to hold tropo sample IDs
    sample_strat = []  # A list to hold strat sample IDs
    # ALL ASVs ARE IN EACH SAMPLE (even if that number is zero)
    # BUT NOT ALL ASVs ARE IN EACH PHENOTYPE

    with open('tax_table_oxy_spore_species.csv') as tax:
        '''
        Open the tax table, iterate through each row. If the 'oxy' condition
        is anaerobe, append the ASV# to the anaerobe list. Likewise for the
        aerobes. Likewise for spore formation.
        '''
        tax_reader = csv.DictReader(tax)
        for row in tax_reader:
            if row['Species'] == "NA":
                pass
            else:
                if row['oxy'] == 'anaerobe':
                    anaer.append(row['X1'])
                elif row['oxy'] == 'aerobe':
                    aer.append(row['X1'])
                if row['spore'] == 'TRUE':
                    spores.append(row['X1'])
                elif row['spore'] == 'FALSE':
                    nospores.append(row['X1'])
                #print(row['X1'], row['oxy'])


    with open('aeroDADA2/sample_data_small.csv') as metadata:
        '''
        Open the metadata file and identify samples that are from
        troposphere, stratosphere, and ground. Append them to a list for future
        reference.
        '''
        meta_reader = csv.DictReader(metadata)
        for row in meta_reader:
            # print(row['characteristic'])
            if row['characteristic'] == 'ground':
                sample_ground.append(row['name'])
            elif row['characteristic'] == 'tropo':
                sample_tropo.append(row['name'])
            elif row['characteristic'] == 'strat':
                sample_strat.append(row['name'])
            else:
                print('sample characteristic not found!')
                sys.exit(1)



    '''Create dictionaries with ASVs and counts for each condition'''
    ground_spores = {}
    strat_spores = {}
    tropo_spores = {}
    ground_nospores = {}
    strat_nospores = {}
    tropo_nospores = {}
    ground_aer = {}
    tropo_aer = {}
    strat_aer = {}
    ground_anaer = {}
    tropo_anaer = {}
    strat_anaer = {}
    ''' Loop through samples, ASVs, partition their counts into phenotype bins
    '''
    with open('aeroDADA2/asv_table.csv') as asv:
        asv_reader = csv.DictReader(asv)
        for row in asv_reader:
            for asv in aer: # partition the aerobes
                if row['X1'] in sample_ground:
                    ground_aer[asv] = int(row[asv])
                if row['X1'] in sample_tropo:
                    tropo_aer[asv] = int(row[asv])
                if row['X1'] in sample_strat:
                    strat_aer[asv] = int(row[asv])
            for asv in anaer: # partition the anaerobes
                if row['X1'] in sample_ground:
                    ground_anaer[asv] = int(row[asv])
                if row['X1'] in sample_tropo:
                    tropo_anaer[asv] = int(row[asv])
                if row['X1'] in sample_strat:
                    strat_anaer[asv] = int(row[asv])
            for asv in spores:
                if row['X1'] in sample_ground:
                    ground_spores[asv] = int(row[asv])
                if row['X1'] in sample_tropo:
                    tropo_spores[asv] = int(row[asv])
                if row['X1'] in sample_strat:
                    strat_spores[asv] = int(row[asv])
            for asv in nospores:
                if row['X1'] in sample_ground:
                    ground_nospores[asv] = int(row[asv])
                if row['X1'] in sample_tropo:
                    tropo_nospores[asv] = int(row[asv])
                if row['X1'] in sample_strat:
                    strat_nospores[asv] = int(row[asv])


    print(ground_spores)
    print(tropo_spores)
    print(strat_spores)
    '''Data to Plot'''
    option = 4 # assign to choose type of plot
    # Oxy Tol
    n_groups = 3
    aer_counts = (sum(ground_aer.values()), sum(tropo_aer.values()),
              sum(strat_aer.values()))
    anaer_counts = (sum(ground_anaer.values()), sum(tropo_anaer.values()),
              sum(strat_anaer.values()))

    total_anaer = sum(anaer_counts)
    total_aer = sum(aer_counts)

    totaL_ground_oxy = (sum(ground_anaer.values()) + sum(ground_aer.values()))
    total_tropo_oxy = (sum(tropo_anaer.values()) + sum(tropo_aer.values()))
    total_strat_oxy = (sum(strat_anaer.values()) + sum(strat_aer.values()))

    aer_ratio = ((aer_counts[0]/totaL_ground_oxy),
                (aer_counts[1]/total_tropo_oxy),
                (aer_counts[2]/total_strat_oxy))

    anaer_ratio = ((anaer_counts[0]/totaL_ground_oxy),
                  (anaer_counts[1]/total_tropo_oxy),
                  (anaer_counts[2]/total_strat_oxy))


    # Spore formation
    spore_counts = (sum(ground_spores.values()), sum(tropo_spores.values()),
              sum(strat_spores.values()))
    nospore_counts = (sum(ground_nospores.values()), sum(tropo_nospores.values()),
              sum(strat_nospores.values()))
    print(spore_counts)

    total_spores = sum(spore_counts)
    total_nospores = sum(nospore_counts)

    totaL_ground_sp = (sum(ground_spores.values()) + sum(ground_nospores.values()))
    total_tropo_sp = (sum(tropo_spores.values()) + sum(tropo_nospores.values()))
    total_strat_sp = (sum(strat_spores.values()) + sum(strat_nospores.values()))

    spore_ratio = ((spore_counts[0]/totaL_ground_sp),
                (spore_counts[1]/total_tropo_sp),
                (spore_counts[2]/total_strat_sp))

    nospore_ratio = ((nospore_counts[0]/totaL_ground_sp),
                  (nospore_counts[1]/total_tropo_sp),
                  (nospore_counts[2]/total_strat_sp))

    objects = ('Ground', 'Troposphere', 'Lower_Stratosphere')
    y_pos = np.arange(len(objects))



    # Oxy Relative
    if option == 1:
        fig, ax = plt.subplots()
        index = np.arange(n_groups)
        bar_width = 0.35
        opacity = 0.8

        rel1 = plt.bar(index, aer_ratio, bar_width,alpha=opacity,color='c',label='Aerobic')
        rel2 = plt.bar(index, anaer_ratio, bar_width,alpha=opacity,color='r',label='Anaerobic', bottom=aer_ratio)

        plt.ylabel('Relative abundance')
        plt.title('Oxygen Tolerance Distribution (Relative)')
        plt.xticks(y_pos, objects)
        plt.legend()
        plt.savefig('aerobes_relative.png', bbox_inches='tight')

    # Oxy Absolute
    if option == 2:
        fig, ax = plt.subplots()
        index = np.arange(n_groups)
        bar_width = 0.35
        opacity = 0.8

        abs1 = plt.bar(index, aer_counts, bar_width,alpha=opacity,color='c',label='Aerobic')
        abs2 = plt.bar(index + bar_width, anaer_counts, bar_width,alpha=opacity,color='r',label='Anaerobic')

        plt.ylabel('Read count')
        plt.title('Oxygen Tolerance Distribution (Absolute)')
        plt.xticks(y_pos, objects)
        plt.legend()
        plt.savefig('aerobes_absolute.png', bbox_inches='tight')

    # Spore Relative
    if option == 3:
        fig, ax = plt.subplots()
        index = np.arange(n_groups)
        bar_width = 0.35
        opacity = 0.8

        rel1 = plt.bar(index, spore_ratio, bar_width,alpha=opacity,color='c',label='Spore')
        rel2 = plt.bar(index, nospore_ratio, bar_width,alpha=opacity,color='r',label='No spores', bottom=spore_ratio)

        plt.ylabel('Relative abundance')
        plt.title('Spore Formation (Relative)')
        plt.xticks(y_pos, objects)
        plt.legend()
        plt.savefig('spore_absolute.png', bbox_inches='tight')

    if option == 4:
        fig, ax = plt.subplots()
        index = np.arange(n_groups)
        bar_width = 0.35
        opacity = 0.8

        abs1 = plt.bar(index, spore_counts, bar_width,alpha=opacity,color='c',label='Spore')
        abs2 = plt.bar(index + nospore_counts, bar_width,alpha=opacity,color='r',label='No spores')

        plt.ylabel('Read count')
        plt.title('Spore Formation (Absolute)')
        plt.xticks(y_pos, objects)
        plt.legend()
        plt.savefig('spore_absolute.png', bbox_inches='tight')

if __name__ == "__main__":
    main()
