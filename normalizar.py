import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datosln.txt', sep=',', header=0)

# copiar los datos
df_z_scaled = df.copy()
  
# normalizar
for column in df_z_scaled.loc[:, 'delta':'high_gamma']:
    df_z_scaled[column] = (df_z_scaled[column] -
                           df_z_scaled[column].mean()) / df_z_scaled[column].std()

df_z_scaled.to_csv('datosn.txt', index=False)