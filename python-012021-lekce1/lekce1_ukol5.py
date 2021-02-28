prodeje2019 = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

prodeje2020 = {
    "Zkus mě chytit": 3157,
    "Vrah zavolá v deset": 3541,
    "Vražda podle knihy": 2510,
    "Past": 2364,
    "Zločinný steh": 5412,
    "Zkus mě chytit": 6671,
}
kniha = input("Zadej název knihy: ")
if kniha in prodeje2019 and prodeje2020:
    sales = prodeje2019[kniha]
    sales += prodeje2020[kniha]
    print(f"{kniha} se prodalo celkem {sales} kusů.")
else:
    sales = prodeje2020[kniha]
    print(f"{kniha} se prodalo celkem {sales} kusů.")



