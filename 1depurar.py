import pandas as pd
import numpy as np

df = pd.read_csv('d2/datos2.txt', sep=',', header=0)

df_d = df.loc[df['signal_strength'] == 0]

df_d.to_csv('d2/datosdep.txt', index=False)