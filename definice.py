import random


# prorovna yadane cislo s hadanim
# a zisti pritomnost stejnich cifer ale na jinich mistech
def najdi_cows(data, cislo):

    cows = []
    if data[0] in cislo and data[0] != cislo[0]:
        cows.append(1)
    if data[1] in cislo and data[1] != cislo[1]:
        cows.append(1)
    if data[2] in cislo and data[2] != cislo[2]:
        cows.append(1)
    if data[3] in cislo and data[3] != cislo[3]:
        cows.append(1)
    return cows


# prorovna yadane cislo s hadanim
# a zisti pritomnost stejnich cifer ale na stejnich mistech
def najdi_bulss(data, cislo):
    bulls = []

    if data[0] == cislo[0]:
        bulls.append(1)
    if data[1] == cislo[1]:
        bulls.append(1)
    if data[2] == cislo[2]:
        bulls.append(1)
    if data[3] == cislo[3]:
        bulls.append(1)
    return bulls


def generuj_cislo(cislo):
    rada = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    while len(cislo) < 4:
        cislo.append(random.choice(rada))
        if cislo[0] == 0:
            cislo[0] = random.choice(rada)

        rada.remove(cislo[0])
        cislo.append(random.choice(rada))

        rada.remove(cislo[1])
        cislo.append(random.choice(rada))

        rada.remove(cislo[2])
        cislo.append(random.choice(rada))


def kontrola_0(data,):  # kontrola na 0
    index = 0
    if data[0] == 0:
        print("pozor! nezacinej 0")
        print("-" * 50)
        index = 1
    if index == 1:
        return index


def kontrola_delka(data, ):  # kontrola na delku cisla
    index = 0
    if len(data) < 4:
        print("kratsi delka.")
        print("-" * 50)
        index = 1

    if len(data) > 4:
        print("delsi delka.")
        print("-" * 50)
        index = 1
    if index == 1:
        return index


def kontrola_duplikat(data):    # kontrola na duplikat
    index = 0
    duplikat = list(dict.fromkeys(data))
    if len(duplikat) != 4:
        print('duplikat')
        print("-" * 50)
        index = 1
    if index == 1:
        return index


# vyhodnoceni vysledku podle poctu pokusu
def pokusi(cislo1, pocet, cilo2, slovo):
    if cislo1 < pocet <= cilo2:
        print("That's ", slovo)
