class Auto:
  def __init__(self, plate, brand, kilometers):
    self.plate = plate
    self.brand = brand
    self.kilometers = kilometers
    self.available = True

  def pujc_auto(self):
    self.available = False

  def getInfo(self):
    if self.available:
      text = "Potvrzuji zapůjčení vozidla."
    else:
      text = "Vozidlo není k dispozici."
    print(f"Registrační značka: {self.plate}, typ vozidla: {self.brand}. {text}")

skoda = Auto("1P3 4747", "Škoda Octavia", 41253)
peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)

vypujcka = input("Zadej značku, kterou si chceš vypůjčit: ")
if vypujcka == "Škoda":
    skoda.getInfo()
    skoda.pujc_auto()
elif vypujcka == "Peugeot":
    peugeot.getInfo()
    peugeot.pujc_auto()
else:
    print("Půjčujeme pouze vozy Škoda nebo Peugeot.")

vypujcka = input("Zadej značku, kterou si chceš vypůjčit: ")
if vypujcka == "Škoda":
    skoda.getInfo()
    skoda.pujc_auto()
elif vypujcka == "Peugeot":
    peugeot.getInfo()
    skoda.pujc_auto()
else:
    print("Půjčujeme pouze vozy Škoda nebo Peugeot.")