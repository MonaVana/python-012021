class Kontakt:
  def __init__(self, jmeno, email):
    self.jmeno = jmeno
    self.email = email

class Uchazec(Kontakt):
  def __init__(self, jmeno, email, datumPohovoru):
    super().__init__(jmeno, email)
    self.datumPohovoru = datumPohovoru
    self.zapisZPohovoru = " "

  def ulozZapis(self):
    from datetime import datetime
    datumPohovoru = input("Zadej datum pohovoru: ")
    datumPohovoru = datetime.strptime(datumPohovoru, "%d. %m. %Y")
    if datumPohovoru <= datetime.now():
      return "Zápis byl uložen"
    else:
      return "Pohovor se ještě nekonal, nelze uložit."

uchazec = Uchazec("Jan Novák", "jannovak@email.cz", "1. 2. 2021")
print(uchazec.ulozZapis())