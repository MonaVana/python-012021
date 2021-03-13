class Auto:
  def availability (self):
    self.available = True
  def getInfo(self):
    if self.available:
      availableText = "Auto je volné."
    else:
      availableText = "Auto je vypůjčené."
  def __init__(self, plate, brand, kilometers):
    self.plat = plate
    self.brand = brand
    self.kilometers = kilometers
    self.available = True

skoda = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
peugeot = Auto("1P3 4747", "Škoda Octavia", 41253)

