from forex_python.converter import CurrencyRates
prevodnik = CurrencyRates()

def convert(cilovaMena, zdrojovaMena, pozadovanoVCiloveMene):
  cenaVeZdrojoveMene = prevodnik.convert(cilovaMena, zdrojovaMena, pozadovanoVCiloveMene)
  return cenaVeZdrojoveMene

zdrojovaMena = input("Z jaké měny převádíš: ")
cilovaMena = input("Jakou chceš měnu: ")
pozadovanoVCiloveMene = int(input("Kolik chceš dostat v cílové měně: "))

print(f"Pro směnu potřebuješ {round(convert(cilovaMena, zdrojovaMena, pozadovanoVCiloveMene), 2)} jednotek měny.")