import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from statsmodels.formula.api import ols
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.stats.diagnostic import het_white
from statsmodels.stats.diagnostic import kstest_normal

def normality_test(lista):

    # Realiza un test de normalidad de Kolmogorov-Smirnnof sobre la variable endógena y muestra una gráfica de
    # distribución

    # Parámetros:
    #       y (Series): Objeto Series de pandas con la variable endógena.

    # Devuelve:
    #       Nada.

        normality_test = kstest_normal(lista, dist='norm')
        stats = ['KS Stat', 'KS-Test p-value']

        print("---Test de Kolmogorov-Smirnnof---")
        print(dict(zip(stats, normality_test)))
        if (normality_test[1] > 0.05):
            print(
                "Aceptamos la hipótesis nula, ergo la variable se distribuye según una normal."
            )
        else:
            print(
                "Fallamos al aceptar la hipótesis nula, ergo la variable no se distribuye según una normal."
            )
        sns.displot(lista)
        plt.show()

df = pd.read_csv('datos.txt', sep=',', header=0)

for col in df.loc[:, 'delta':'high_gamma']:
    normality_test(df[col])