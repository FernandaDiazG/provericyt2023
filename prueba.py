import statsmodels.api as sm
import pandas as pd

df = pd.read_csv('datosln.txt', sep=',', header=0)

for col in df.loc[:, 'delta':'high_gamma']:
    # lista = df[col].tolist()
    # k = sm.stats.diagnostic.kstest_normal(lista, dist='norm', pvalmethod='table')
    # print(k)
    print(sm.stats.diagnostic.kstest_normal(df[col], dist='norm', pvalmethod='table'))