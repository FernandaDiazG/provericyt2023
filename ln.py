import pandas as pd
import numpy as np

df = pd.read_csv('datosdep.txt', sep=',', header=0)

df.loc[:, 'delta':'high_gamma']=df.loc[:, 'delta':'high_gamma'].apply(np.log)

df.to_csv('datosln.txt', index=False)