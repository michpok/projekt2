import random


# prorovna yadane cislo s hadanim
# a zisti pritomnost stejnich cifer ale na jinich mistech
def find_cows(data, cislo, cow):

    if data[0] in cislo and data[0] != cislo[0]:
        cow.append(1)
    if data[1] in cislo and data[1] != cislo[1]:
        cow.append(1)
    if data[2] in cislo and data[2] != cislo[2]:
        cow.append(1)
    if data[3] in cislo and data[3] != cislo[3]:
        cow.append(1)
    return cow


# prorovna yadane cislo s hadanim
# a zisti pritomnost stejnich cifer ale na stejnich mistech
def find_bulss(data, cislo, bull):

    if data[0] == cislo[0]:
        bull.append(1)
    if data[1] == cislo[1]:
        bull.append(1)
    if data[2] == cislo[2]:
        bull.append(1)
    if data[3] == cislo[3]:
        bull.append(1)
    return bull


def number_generator(number):
    number_range = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    number.append(random.choice(number_range))
    number_range.append(0)

    number_range.remove(number[0])
    number.append(random.choice(number_range))

    number_range.remove(number[1])
    number.append(random.choice(number_range))

    number_range.remove(number[2])
    number.append(random.choice(number_range))


def check_0(data,):  # kontrola na 0
    if data[0] == 0:
        print("wait! dont start with 0")
        print("-" * 50)
        index = 1
        return index


def check_length(data, ):  # kontrola na delku cisla
    if len(data) < 4:
        print("it is shorter number.")
        print("-" * 50)
        index = 1
        return index

    if len(data) > 4:
        print("it is longer number.")
        print("-" * 50)
        index = 1
        return index


def check_duplicate(data):    # kontrola na duplikat
    duplikat = list(dict.fromkeys(data))
    if len(duplikat) != 4:
        print('duplicate')
        print("-" * 50)
        index = 1
        return index


# vyhodnoceni vysledku podle poctu pokusu
def attempt(cislo1, pocet, cislo2, slovo):
    if cislo1 < pocet <= cislo2:
        print("That's ", slovo)
        exit()


def singular_plural_words(data, word_list, text1, text2):

    if len(data) == 1:
        word_list.append(text1)
    else:
        word_list.append(text2)

    return word_list
