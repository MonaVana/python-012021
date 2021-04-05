#import wget

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/staty.json")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/gdp.csv")

import pandas
staty = pandas.read_json("staty.json")
staty = staty.set_index("region")

print(staty.loc["Europe"])
subregiony_evropy = staty.loc["Europe"]
print(subregiony_evropy.groupby("subregion")["name"].count())
print(subregiony_evropy.groupby("subregion")["population"].sum())

#doplnek
gdp = pandas.read_csv("gdp.csv").dropna()
staty = staty.rename(columns={"alpha3Code":"Country Code"})
gdp_staty = pandas.merge(staty, gdp, on="Country Code", how="left")
gdp_staty["gdp_per_capita"] = gdp_staty["2019"] / gdp_staty["population"]
print(gdp_staty.groupby("subregion")[["population", "2019", "gdp_per_capita"]].sum())