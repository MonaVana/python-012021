#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")

import matplotlib.pyplot as plt
import pandas

teploty = pandas.read_csv("temperature.csv")

teplota_mesta = teploty[teploty["City"].isin(["Helsinki", "Miami Beach", "Tokyo"])][["City", "AvgTemperature"]]


teplota_mesta.boxplot(whis=[0, 100], by="City")
plt.show()