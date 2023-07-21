import statsmodels.api as sm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('datosdep.txt', sep=',', header=0)

for col in df.loc[:, 'delta':'high_gamma']:
    # lista = df[col].tolist()
    # k = sm.stats.diagnostic.kstest_normal(lista, dist='norm', pvalmethod='table')
    # print(k)
    print(sm.stats.diagnostic.kstest_normal(df[col], dist='norm', pvalmethod='table'))