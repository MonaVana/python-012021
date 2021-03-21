class Polozka:
  def __init__(self, nazev, zanr):
    self.nazev = nazev
    self.zanr = zanr

  def getInfo(self):
    return f"Název: {self.nazev}, žánr: {self.zanr}"

class Film(Polozka):
  def __init__(self, nazev, zanr, delka):
    super().__init__(nazev, zanr)
    self.delka = delka

  def getInfo(self):
    return f"{super().getInfo()}, délka filmu: {self.delka} min."

class Serial(Polozka):
  def __init__(self, nazev, zanr, pocetEpizod, delkaEpizody):
    super().__init__(nazev, zanr)
    self.pocetEpizod = pocetEpizod
    self.delkaEpizody = delkaEpizody

  def getInfo(self):
    return f"{super().getInfo()}, počet epizod seriálu: {self.pocetEpizod}, délka epizody: {self.delkaEpizody}"

film = Film("Kmotr", "drama", 175)
print(film.getInfo())

serial = Serial("Přátelé", "komedie", 236, 22)
print(serial.getInfo())