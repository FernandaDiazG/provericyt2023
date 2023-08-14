import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import cycle

df = pd.read_csv('d1/datosesc.txt', sep=',', header=0)

fig, axes = plt.subplots(nrows=2, ncols=5)
colors = cycle(sns.color_palette('hls', 10))

for (axe,col) in zip(axes.flat,df.loc[:,'attention':'high_gamma']):
    sns.histplot(df[col], ax=axe, bins=25, kde=True, color=next(colors))

plt.show()
