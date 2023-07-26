import pandas as pd
import numpy as np

##### depurar
df = pd.read_csv('datos3.txt', sep=',', header=0)

df_d = df.loc[df['signal_strength'] == 0]

df_d.to_csv('datosdep.txt', index=False)

#### logaritmo

df_d.loc[:, 'delta':'high_gamma']=df_d.loc[:, 'delta':'high_gamma'].apply(np.log)

df_d.to_csv('datosln.txt', index=False)

#### estandarizar

df_z = df_d.copy()
  
for column in df_z.loc[:, 'delta':'high_gamma']:
    df_z[column] = (df_z[column] -
                           df_z[column].mean()) / df_z[column].std()

df_z.to_csv('datosn.txt', index=False)

#### escalar

df_esc = pd.DataFrame(df_z.loc[:, 'signal_strength':'meditation'])

for col in df.loc[:, 'delta':'high_gamma']:
    min = df[col].min()
    max = df[col].max()
    m = (0 - 100)/(min - max)
    x = df[col]
    y = m * (x - min)
    df_esc[col] = y

df_esc.to_csv('datosesc.txt', index=False)

