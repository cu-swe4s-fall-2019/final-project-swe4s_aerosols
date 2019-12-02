import math
import os
from os import path
import sys
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')


def boxplot(L, out_file_name, groups, gene_name, group_col_name):
    if path.exists(out_file_name):
        raise OSError("File path already exists!")
        sys.exit(1)

    if L is None:
        raise ValueError("Can't graph None!")

    if L == []:
        raise ValueError("Can't graph an empty list!")
    try:
        for line in L:
            k = line[1]
    except IndexError:
        print("Can't plot 1D data!")

    data = []
    for l in L:
        try:
            data.append(l)
        except ValueError:
            print("Something went wrong with a certain list.")
            continue

    fig, ax1 = plt.subplots(figsize=(10, 6))
    fig.canvas.set_window_title('A Boxplot Example')
    plt.subplots_adjust(left=0.075, right=0.95, top=0.9, bottom=0.25)

    ticks = []
    k = 1

    for i in groups:
        ticks.append(k)
        k += 1

    bp = plt.boxplot(data, notch=0, vert=1, whis=1.5)
    plt.setp(bp['boxes'], color='black')
    plt.setp(bp['whiskers'], color='black')
    plt.setp(bp['fliers'], color='red', marker='+')
    plt.ylabel('Gene Read Counts')
    plt.xlabel(group_col_name)
    plt.title(gene_name)
    plt.xticks(ticks, groups, rotation='vertical')
    plt.savefig(out_file_name, bbox_inches='tight')


def histogram(L, out_file_name):
    if path.exists(out_file_name):
        raise OSError("File path already exists!")
        sys.exit(1)
    if L is None:
        raise ValueError("Can't graph None!")

    if L == []:
        raise ValueError("Can't graph an empty list!")

    try:
        for line in L:
            k = line[1]
    except TypeError:
        print("Can't plot 1D data!")

    D = []
    y = []
    for l in L:
        D.append(float(l[0]))
        D.append(float(l[1]))
        y.append(float(l[1]))

    width = 3
    height = 3
    stat_mean = str(ml.list_mean(y))
    stat_stdev = str(ml.list_stdev(y))
    fig = plt.figure(figsize=(width, height), dpi=300)
    ax = fig.add_subplot(1, 1, 1)
    ax.hist(D)
    plt.title("Mean: " + stat_mean + " " + "stdev: " + stat_stdev)
    plt.ylabel('Frequency')
    plt.savefig(out_file_name, bbox_inches='tight')


def combo(L, out_file_name):
    if path.exists(out_file_name):
        raise OSError("File path already exists!")
        sys.exit(1)

    if L is None:
        raise ValueError("Can't graph None!")

    if L == []:
        raise ValueError("Can't graph an empty list!")

    try:
        for line in L:
            k = line[1]
    except TypeError:
        print("Can't plot 1D data!")

    D = []
    x = []
    y = []

    for l in L:
        D.append(float(l[0]))
        D.append(float(l[1]))
        x.append(float(l[0]))
        y.append(float(l[1]))

    stat_mean = str(ml.list_mean(y))
    stat_stdev = str(ml.list_stdev(y))
    width = 5
    height = 3

    fig = plt.figure(figsize=(width, height), dpi=300)
    ax = fig.add_subplot(1, 2, 1)
    ax.boxplot(x, y, '.')
    ax = fig.add_subplot(1, 2, 2)
    ax.hist(D)
    plt.title("Mean: " + stat_mean + " " + "stdev: " + stat_stdev)
    plt.ylabel('Frequency')
    plt.savefig(out_file_name, bbox_inches='tight')
