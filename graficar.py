import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('datosesc.txt', sep=',', header=0)

print(df.dtypes)

attention = ['attention',
          'low_beta',
          'high_beta',
          'low_gamma',
          'high_gamma']

meditation = ['meditation','delta','theta','low_alpha','high_alpha']

fig, axes = plt.subplots(nrows=2, ncols=1)

df.loc[:,attention].plot(ax=axes[0])
df.loc[:,meditation].plot(ax=axes[1])

plt.show()