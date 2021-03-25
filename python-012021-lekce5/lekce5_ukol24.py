#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")

import pandas
teplota = pandas.read_csv("temperature.csv")

#print(teplota.head())

#teplota = teplota.set_index("City")
#print(teplota.loc["Prague"])

#mereni = teplota[teplota["AvgTemperature"] > 80]
#print(mereni)

#mereni = teplota[(teplota["Region"] == "Europe") & (teplota["AvgTemperature"] > 60)]
#print(mereni)

mereni = teplota[(teplota["AvgTemperature"] > 80) | (teplota["AvgTemperature"] < -20)]
print(mereni)