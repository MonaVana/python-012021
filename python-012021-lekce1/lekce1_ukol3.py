volnePokoje = {
  9: ["Amadeus", "Goya", "Vlasy"],
  10: ["Forman", "Goya"],
  11: [],
  12: ["Amadeus", "Vlasy"]
}
cisloHodiny = int(input("V kolik hodin si chceš zamluvit pokoj: "))
if cisloHodiny in volnePokoje:
  pocetPokoju = volnePokoje[cisloHodiny]
  print(f"V {cisloHodiny} hodin je počet pokojů volných: {len(pocetPokoju)}")
else:
  print("Špatná hodnota")

