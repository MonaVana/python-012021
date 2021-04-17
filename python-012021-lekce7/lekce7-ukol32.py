#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/platy_2021_02.csv")

import matplotlib.pyplot as plt
import pandas
platy = pandas.read_csv("platy_2021_02.csv")

df = platy["plat"]

df.hist(bins=[30000, 35000, 40000, 45000, 50000, 55000, 60000])
plt.show()
