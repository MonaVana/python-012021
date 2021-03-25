#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/country_vaccinations.csv")

import pandas
ockovani = pandas.read_csv("country_vaccinations.csv")

#print(ockovani.head())

#poctyOckovanych = ockovani[ockovani["date"] == "2021-03-10"]
#print(poctyOckovanych[["country", "total_vaccinations"]])

#poctyOckovanych = ockovani[(ockovani["date"] == "2021-03-10") & (ockovani["total_vaccinations"] > 1_000_000)]
#print(poctyOckovanych)

poctyOckovanych = ockovani[(ockovani["daily_vaccinations"] > 100000) | (ockovani["daily_vaccinations"] < 100000)]
print(poctyOckovanych[["country", "date", "daily_vaccinations"]])