import statsmodels.api as sm
import pandas as pd

df = pd.read_csv('dcompletos/datosesc.txt', sep=',', header=0)

y = df.loc[:,'attention']
x = df.loc[:,['delta','theta','low_alpha','high_alpha','high_beta','low_gamma']]

model = sm.OLS(y, x)
results = model.fit()
print(results.summary())
