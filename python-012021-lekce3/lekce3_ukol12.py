class Auto:
  def __init__(self, plate, brand, kilometers):
    self.plate = plate
    self.brand = brand
    self.kilometers = kilometers
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


skoda = Auto("1P3 4747", "Škoda Octavia", 41253)
peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)


def kontrola(vypujcka):
  if vypujcka == "Škoda":
    return skoda.getInfo()
  elif vypujcka == "Peugeot":
    return peugeot.getInfo()
  else:
    return "Půjčujeme pouze vozy Škoda nebo Peugeot."


print(kontrola("Škoda"))
print(kontrola("Audi"))
print(kontrola("Škoda"))
print(kontrola("Peugeot"))
print(kontrola("Peugeot"))
