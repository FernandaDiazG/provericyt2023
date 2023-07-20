import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datos.txt', sep=',', header=0)

# copiar los datos
df_z_scaled = df.copy()
  
# normalizar
for column in df_z_scaled.loc[:, 'delta':'high_gamma']:
    df_z_scaled[column] = (df_z_scaled[column] -
                           df_z_scaled[column].mean()) / df_z_scaled[column].std()


#export DataFrame to text file
with open('datos.txt', 'a') as f:
    df_string = df.to_csv(index=False)
    f.write(df_string)

#export DataFrame to text file
with open('datosz.txt', 'a') as f:
    df_string = df_z_scaled.to_csv(index=False)
    f.write(df_string)
  
# graficar 

df_z_scaled.drop('signal_strength', axis=1).plot(kind='line')

plt.show()