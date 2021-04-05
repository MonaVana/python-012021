#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")

import pandas
teploty = pandas.read_csv("temperature.csv")

teploty.info

#print(teploty[teploty["Day"] == 13])
neplatne_teploty = teploty[teploty["AvgTemperature"] != -99]
#print(neplatne_teploty)
print(teploty.groupby("Region")["Day"].count())
print(teploty.groupby("Region")["AvgTemperature"].mean())
print(neplatne_teploty.groupby("Region")["AvgTemperature"].min())
print(teploty.groupby("Region")["AvgTemperature"].max())
