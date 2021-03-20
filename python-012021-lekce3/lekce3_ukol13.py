class Auto:
  def __init__(self, plate, brand, kilometers, tachometr):
    self.plate = plate
    self.brand = brand
    self.kilometers = kilometers
    self.tachometr = tachometr
    self.available = True

  def pujc_auto(self):
    if self.available:
      self.available = False
      text = "Potvrzuji zapůjčení vozidla."
    else:
      text = "Vozidlo není k dispozici."
    return text

  def getInfo(self):
    return f"Registrační značka: {self.plate}, typ vozidla: {self.brand}. {self.pujc_auto()}"

  def vrat_auto(self, tachometr, pocetDni):
    self.tachometr = tachometr
    if pocetDni <= 7:
      cena = pocetDni * 400
    else:
      cena = pocetDni * 300
    self.available = True
    return f"Cena za půjčení auta je: {cena}"

skoda = Auto("1P3 4747", "Škoda Octavia", 41253, 42000)
peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534, 48000)

tachometr = int(input("Zadej počet ujetých kilometrů: "))
pocetDni = int(input("Zadej počet dnů výpujčky: "))
print(skoda.vrat_auto(tachometr, pocetDni))
print(peugeot.vrat_auto(tachometr,pocetDni))