def obodujZakazku(industry, sales, country, conference=False, newsletter=False):
  totalPoints = 0
  industry = input("Zadej odvětví: ")
  if industry == "automotive":
    totalPoints += 3
  elif industry == "retail":
    totalPoints += 2
  else:
    totalPoints = 0

  sales = int(input("Zadej obrat v mil. EUR: "))
  if sales > 1000:
    totalPoints += 1
  elif 10 < sales <= 1000:
    totalPoints += 3
  else:
    totalPoints = 0

  country = input("Zadej zemi: ")
  if country == "Czechia" or "Slovakia":
    totalPoints += 2
  elif country == "France" or "Germany":
    totalPoints += 1
  else:
    totalPoints = 0

  conference = input("Byl jsi na konferenci: [ano/ne]")
  if conference == "ano":
    conference = True
    totalPoints += 1
  else:
    conference = False
    totalPoints = 0

 newsletter = input("Odebíráš newsletter: [ano/ne]")
  if newsletter == "ano":
    newsletter = True
    totalPoints += 1
  else:
    newsletter = False
    totalPoints = 0

  return totalPoints

totalPoints = obodujZakazku("industry", "sales", "country")
if totalPoints <= 5:
  print(f"Bodový zisk: {totalPoints}. Šance na získání zakázky je malá.")
elif 5 < totalPoints <= 8:
 print(f"Bodový zisk: {totalPoints}. Šance na získání zakázky je střední.")
else:
  print(f"Bodový zisk: {totalPoints}. Šance na získání zakázky je vysoká.")
