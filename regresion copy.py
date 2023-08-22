import statsmodels.api as sm
import pandas as pd
import numpy as np

df = pd.read_csv('d1/datosesc.txt', sep=',', header=0)

y = df.loc[:,'attention']
## x = df.loc[:,['delta','theta','low_alpha','high_alpha','high_beta','low_gamma']]
x = df.loc[:,'delta':'high_gamma']

model = sm.OLS(y, x)
results = model.fit()
print(results.summary())
params = results.params

df_reg = df.loc[:,'attention'].to_frame().copy()
model = (
    params[0]*df['delta'] + 
    params[1]*df['theta']+ 
    params[2]*df['low_alpha'] + 
    params[3]*df['high_alpha'] +
    params[4]*df['high_beta'] +
    params[5]*df['low_gamma']
    )

df_reg['model'] = model
df_reg['exp'] = np.exp(model)
df_reg['diff'] = y - model

df_reg.to_csv('d1/modelo4.txt', index=False)
