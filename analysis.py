import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

table = pd.read_csv("asv_table.csv")
table.head()

ind = np.arange(30)
width = 0.3

teamColours = ['#FF0000','#FF0000','#00FF00','#00FF00',
              '#0000FF','#0000FF','#FF0000','#FF0000',
               '#00FF00','#00FF00','#0000FF','#0000FF',
               '#FF0000','#FF0000','#00FF00','#00FF00',
               '#0000FF','#0000FF','#FF0000','#FF0000',
              '#00FF00','#00FF00','#0000FF','#0000FF',
               '#000000','#000000','#ff00ff','#ff00ff',
               '#24fff0','#24fff0']            
             

plt.bar(x=np.arange(1,31),height=table['ASV6'], color = teamColours)

plt.title("Species: Bacillus")
plt.xlabel("Sample Number")
plt.ylabel("Bacillus Count")

