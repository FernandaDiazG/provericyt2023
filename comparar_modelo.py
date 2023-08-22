import statsmodels.api as sm
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('d1/modelo4.txt', sep=',', header=0)

sns.scatterplot(df,x = 'attention', y = 'exp')

plt.show()

