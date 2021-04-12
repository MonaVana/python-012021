class Polozka:
  def __init__(self, nazev, zanr):
    self.nazev = nazev
    self.zanr = zanr

class Film(Polozka):
  def __init__(self, nazev, zanr, delka):
    super().__init__(nazev, zanr)
    self.delka = delka

  def getCelkovaDelka(self):
    celkovaDelka = self.delka
    return celkovaDelka

class Serial(Polozka):
  def __init__(self, nazev, zanr, pocetEpizod, delkaEpizody):
    super().__init__(nazev, zanr)
    self.pocetEpizod = pocetEpizod
    self.delkaEpizody = delkaEpizody

  def getCelkovaDelka(self):
    celkovaDelka = self.pocetEpizod * self.delkaEpizody
    return celkovaDelka

class Uzivatel:
  def __init__(self, uzivatelskeJmeno):
    self.uzivatelskeJmeno = uzivatelskeJmeno
    self.delkaSledovani = 0

  def pripoctiZhlednuti(self, celkovaDelka):
    self.delkaSledovani += celkovaDelka.getCelkovaDelka()

  def getInfo(self):
    return f"Uživatel {self.uzivatelskeJmeno} zhlédl celkem {self.delkaSledovani} minut."

film = Film("Kmotr", "drama", 175)
serial = Serial("Přátelé", "komedie", 236, 22)
uzivatel = Uzivatel("Jan Novák")
#print(film.getCelkovaDelka())
#print(serial.getCelkovaDelka())
uzivatel.pripoctiZhlednuti(film)
print(uzivatel.getInfo())
uzivatel.pripoctiZhlednuti(serial)
print(uzivatel.getInfo())

