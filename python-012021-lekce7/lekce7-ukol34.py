#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/7/velikonoce.csv")

import matplotlib.pyplot as plt
import pandas
velikonoce = pandas.read_csv("velikonoce.csv")

ax = velikonoce.plot.bar("Datum", "Počet")
ax.set_ylabel("Počet dnů")
plt.show()
