from datetime import datetime
datumPrijezdu = input("Zadej datum: ")
datumPrijezdu = datetime.strptime(datumPrijezdu, "%d. %m. %Y")

prvniTermin = datetime(2021, 7, 1)
druhyTermin = datetime(2021, 8, 10)
tretiTermin = datetime(2021, 8, 11)
cvrtyTermin = datetime(2021, 8, 31)

if(prvniTermin <= datumPrijezdu <= druhyTermin):
  pocetOsob = int(input("Zadej počet osob: "))
  cenaUbytovaní = pocetOsob * 250
  print(f"Cena ubytování bude: {cenaUbytovaní}")
elif(tretiTermin <= datumPrijezdu <= cvrtyTermin):
  pocetOsob = int(input("Zadej počet osob: "))
  cenaUbytovani = pocetOsob * 180
  print(f"Cena ubytování bude: {cenaUbytovani}")
else:
  print("Letní kino je v tomto termínu uzavřené.")