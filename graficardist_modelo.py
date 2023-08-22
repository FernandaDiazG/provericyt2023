import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import cycle

df = pd.read_csv('d1/modelo.txt', sep=',', header=0)

fig, axes = plt.subplots(nrows=1, ncols=2)
colors = cycle(sns.color_palette('hls', 10))

for (axe,col) in zip(axes.flat,df.loc[:,:]):
    sns.histplot(df[col], ax=axe, bins=25, kde=True, color=next(colors))

plt.show()
