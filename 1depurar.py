import pandas as pd
import numpy as np

df = pd.read_csv('datos3.txt', sep=',', header=0)

df_d = df.loc[df['signal_strength'] == 0]

df_d.to_csv('datosdep.txt', index=False)