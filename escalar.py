import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('datosz.txt', sep=',', header=0)

df_esc = pd.DataFrame(df.loc[:, 'signal_strength':'meditation'])

for col in df.loc[:, 'delta':'high_gamma']:
    min = df[col].min()
    max = df[col].max()
    m = (0 - 100)/(min - max)
    x = df[col]
    y = m * (x - min)
    df_esc[col] = y

df_esc.to_csv('datosesc.txt', index=False)