vysledky = [
  {"Jméno": "Mirek Dušín", "Český jazyk": 1, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 1, "Zeměpis": 1},
  {"Jméno": "Jarka Metelka", "Český jazyk": 3, "Anglický jazyk": 1, "Matematika": 3, "Dějepis": 2, "Ekonomika": 5},
  {"Jméno": "Jindra Hojer", "Český jazyk": 2, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 3, "Chemie": 3},
  {"Jméno": "Červenáček", "Český jazyk": 1, "Anglický jazyk": 1, "Matematika": 1, "Fyzika": 2, "Informatika": 4},
  {"Jméno": "Rychlonožka", "Český jazyk": 4, "Anglický jazyk": 3, "Matematika": 2, "Chemie": 1, "Biologie": 4},
]

def ohodnot_studenta(sumOfMarks):
  sumOfMarks = {}
  for item in vysledky:
    student = item["Jméno"]
    mark = item.pop("Jméno")
    if student in sumOfMarks:
      sumOfMarks[student] += mark
    else:
      sumOfMarks[student] = mark

  totalMark = 0
  for mark in sumOfMarks.values():
    totalMark += mark
    averageMark = totalMark / len(sumOfMarks)

  if averageMark <= 1.5 and mark != 3:
    return f"{student}: Prospěl s vyznamenáním"
  elif mark == 5:
    return f"{student}: Neprospěl"
  else:
    return f"{student}: Prospěl"


