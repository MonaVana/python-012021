#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")

import pandas
teploty = pandas.read_csv("temperature.csv")

#teploty[teploty["Day"] == 13]
neplatne_teploty = teploty[teploty["AvgTemperature"] != -99]
#print(neplatne_teploty.sort_values(by="AvgTemperature", ascending=False))
print(neplatne_teploty.groupby("City")["AvgTemperature"].mean().sort_values(ascending=False)[:5])
print(neplatne_teploty.groupby("City")["AvgTemperature"].mean().sort_values()[:5])


