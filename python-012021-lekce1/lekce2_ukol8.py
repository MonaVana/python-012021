def phoneVerification(phoneNumber):
  if len(phoneNumber) == 9:
    return True
  elif len(phoneNumber) == 13:
    return True
  else:
    return False
phoneNumber = input("Zadej telefonní číslo: ")
phoneNumber = phoneNumber.replace(" ", "")
verified = phoneVerification(phoneNumber)
if verified:
    textSMS = input("Zadej text zprávy: ")
    def textPrice (textSMS):
      import math
      zprava = math.ceil(len(textSMS)/180)
      cena = zprava * 3
      return cena
    cena = textPrice(textSMS)
    print(f"Výsledná cena SMS je {cena} Kč.")
else:
  print("Chyba ověření. Zadej číslo znovu.")
