#import wget

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_praha.csv")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_plzeň.csv")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_liberec.csv")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/platy_2021_02.csv")

import pandas
praha = pandas.read_csv("zam_praha.csv")
plzen = pandas.read_csv("zam_plzeň.csv")
liberec = pandas.read_csv("zam_liberec.csv")
platy = pandas.read_csv("platy_2021_02.csv")

praha["mesto"] = "Praha"
plzen["mesto"] = "Plzeň"
liberec["mesto"] = "Liberec"

zamestnanci = pandas.concat([praha, plzen, liberec], ignore_index=True)

platy_zamestnancu = pandas.merge(zamestnanci, platy, on=["cislo_zamestnance"], how="left")

print(platy_zamestnancu.groupby("mesto")["plat"].mean().dropna())

#doplněk
uz_nejsou_zamestnanci = platy_zamestnancu[platy_zamestnancu["plat"].isnull()]
print(uz_nejsou_zamestnanci)
uz_nejsou_zamestnanci.to_csv("uz nejsou zamestanci.csv", index=False)
