import pandas
teplota = pandas.read_csv("temperature.csv")

#teploty = teplota[teplota["Day"] == 13]
#print(teploty)

teplota_US = teplota[(teplota["Day"] == 13) & (teplota["Country"] == "US")]
#print(teplota_US)

teplota_US_city = teplota_US[teplota_US["City"].isin(["Washington", "Philadelphia"])]
print(teplota_US_city)