baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}
kodBaliku = input ("Zadej kód balíku: ")
if kodBaliku in baliky:
    if baliky[kodBaliku]:
        print ("Balík byl předán kurýrovi")
    else:
        print ("Balík zatím nebyl předán kurýrovi")
else:
    print("Špatná hodnota.")