import statsmodels.api as sm
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('d1/datosesc.txt', sep=',', header=0)

pc = sm.multivariate.PCA(df.loc[:,'delta':'high_gamma'])

pc.plot_scree()
print(pc.factors)
print(pc.weights)
plt.show()