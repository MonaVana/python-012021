#import wget

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/vykazy.csv")

import pandas
praha = pandas.read_csv("zam_praha.csv")
plzen = pandas.read_csv("zam_plzeň.csv")
liberec = pandas.read_csv("zam_liberec.csv")
platy = pandas.read_csv("platy_2021_02.csv")
vykazy = pandas.read_csv("vykazy.csv")

print(vykazy.groupby("project")["hours"].sum())

#doplněk
praha["mesto"] = "Praha"
plzen["mesto"] = "Plzeň"
liberec["mesto"] = "Liberec"

zamestnanci = pandas.concat([praha, plzen, liberec], ignore_index=True)

platy_zamestnancu = pandas.merge(zamestnanci, platy, on=["cislo_zamestnance"], how="left")
vykazy = vykazy.rename(columns={"emloyee_id":"cislo_zamestnance"})


hodiny_na_projekt = pandas.merge(platy_zamestnancu, vykazy, on=["cislo_zamestnance"], how="left")
print(hodiny_na_projekt.groupby("mesto")["hours"].sum())

