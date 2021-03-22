#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/character-deaths.csv")


import pandas
got = pandas.read_csv("character-deaths.csv")
got = got.set_index("Name")


#got.info()
#got.index
#print(got.loc["Hali"])
#print(got.loc["Gevin Harlaw" : "Gillam"])
#print(got.loc["Gevin Harlaw" : "Gillam", "Death Year"])
print(got.loc["Gevin Harlaw" : "Gillam", "GoT" : "DwD"])