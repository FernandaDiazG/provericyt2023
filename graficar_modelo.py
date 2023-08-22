import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import cycle
from matplotlib.widgets import Slider

df = pd.read_csv('d1/modelo4.txt', sep=',', header=0, nrows=600)

attention = ['attention',
          'low_beta',
          'high_beta',
          'low_gamma',
          'high_gamma']

meditation = ['meditation',
              'delta',
              'theta',
              'low_alpha',
              'high_alpha']

fig, axes = plt.subplots(nrows=4, ncols=1)
plt.subplots_adjust(bottom=0.25)

plt.setp(axes, xlim=(0,300))

colors = cycle(sns.color_palette('hls', 10))

for (axe,col) in zip(axes.flat,df.loc[:,:]):
    sns.lineplot(df[col], ax= axe, color=next(colors))

axpos = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor="white")

spos = Slider(axpos, 'Pos', 0, df.shape[0]-300)

def update(val):
    pos = spos.val
    plt.setp(axes, xlim=(pos, pos+300))
    fig.canvas.draw_idle()

spos.on_changed(update)

plt.show()
