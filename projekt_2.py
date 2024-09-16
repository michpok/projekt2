"""
projekt_2.py: druhy projekt do Engeto Online Python Akademie
author: Michal Pokorný
email: my.pokorny@gmail.com
discord: mipok
"""
import math
from definice import (najdi_cows, najdi_bulss, generuj_cislo,
                      kontrola_0, kontrola_delka,
                      kontrola_duplikat, pokusi)

print("Hi there!", "\n", "-"*50)

# generace cisla
cislo = []
generuj_cislo(cislo)

# hrajem
print("I've generated a random 4 digit number for you.""\n""Let's play a bulls and cows game.",
      "\n", "-"*50, "\n" "Enter a number:" "\n", "-"*50)

# zpracovani hadaneho cisla
zpracovaneCislo = []
pocitadlo = 0
while zpracovaneCislo != cislo:

    zpracovaneCislo = []
    hadaneCislo = []
    hadaneCisla = input()
    pocitadlo = pocitadlo + 1

    # kontrola na existenci pismen
    if not hadaneCisla.isnumeric():
        print("neni cislo", "\n", "-" * 50)
        continue
    hadaneCislo.append(hadaneCisla)

    # zpracovani cisla do listu
    hadaneCislo_str = str(hadaneCislo[0])
    for zpracovani in hadaneCislo_str:
        zpracovaneCislo.append(int(zpracovani))

    # kontrola cifer
    if kontrola_0(zpracovaneCislo) == 1:
        continue
    if kontrola_delka(zpracovaneCislo) == 1:
        continue
    if kontrola_duplikat(zpracovaneCislo) == 1:
        continue

    # fuze elementu listu do jednoho elemntu
    vypis = [str(i) for i in zpracovaneCislo]
    vypis2 = int("".join(vypis))

    if zpracovaneCislo != cislo:
        print(">>>", vypis2, "\n",
              len(najdi_bulss(zpracovaneCislo, cislo)), "bull",
              len(najdi_cows(zpracovaneCislo, cislo)), "cows", "\n", "-"*50)
    else:
        print(">>>", vypis2, "\n", "Correct, you've guessed the right number")

print('Total number of guesses:', pocitadlo, "\n", "-"*50)

# hodnoceni
pokusi(0, pocitadlo, 10, 'amazing')
pokusi(10, pocitadlo, 20, 'average')
pokusi(20, pocitadlo, math.inf, 'not so good')