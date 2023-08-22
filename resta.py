import statsmodels.api as sm
import pandas as pd

df = pd.read_csv('d1/modelo2.txt', sep=',', header=0)

y = df.loc[:,'attention']
## x = df.loc[:,['delta','theta','low_alpha','high_alpha','high_beta','low_gamma']]
x = df.loc[:,'model']


df_res = y-x

df['diff'] = df_res

df.to_csv('d1/modelo3.txt', index=False)