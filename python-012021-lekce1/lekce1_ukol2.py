sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}
kodSoucastky = input("Zadej kód součástky: ")
mnozstvi = int(input("Kolik si chce koupit: "))
if kodSoucastky not in sklad:
    print(f"Součástka {kodSoucastky} není skladem.")
elif sklad[kodSoucastky] <= mnozstvi:
    print(f"Součástka {kodSoucastky} je skladem, ale max. v počtu {sklad.pop(kodSoucastky)} ks.")
else:
    sklad[kodSoucastky] -= mnozstvi
    print(f"Součástky {kodSoucastky} lez objednat. Na skladě zbyde {sklad[kodSoucastky]} ks.")
