"""
projekt_2.py: druhy projekt do Engeto Online Python Akademie
author: Michal Pokorný
email: my.pokorny@gmail.com
discord: michalpokorny.
"""
import math
from definice import (find_cows, find_bulss, number_generator,
                      check_0, check_length,
                      check_duplicate, attempt)

print("Hi there!", "\n", "-"*50)

# generace cisla
number = []
number_generator(number)

# hrajem
print("I've generated a random 4 digit number for you.""\n""Let's play a bulls and cows game.",
      "\n", "-"*50, "\n" "Enter a number:" "\n", "-"*50)

# zpracovani hadaneho cisla
procesingNumber = []
counter = 0
while procesingNumber != number:

    procesingNumber = []
    guessNumber = []
    hadaneCisla = input()
    counter = counter + 1

    # kontrola na existenci pismen
    if not hadaneCisla.isnumeric():
        print("neni cislo", "\n", "-" * 50)
        continue
    guessNumber.append(hadaneCisla)

    # zpracovani cisla do listu
    guessNumber_str = str(guessNumber[0])
    for procesing in guessNumber_str:
        procesingNumber.append(int(procesing))

    # kontrola cifer
    if check_0(procesingNumber) == 1:
        continue
    if check_length(procesingNumber) == 1:
        continue
    if check_duplicate(procesingNumber) == 1:
        continue

    # fuze elementu listu do jednoho elemntu
    final_procesing = [str(i) for i in procesingNumber]
    find_out_number = int("".join(final_procesing))

    bulls = []
    find_bulss(procesingNumber, number, bulls)

    if len(bulls) == 1:
        wordBulls = 'bull'
    else:
        wordBulls = 'bulls'

    cows = []
    find_cows(procesingNumber, number, cows)
    if len(cows) == 1:
        wordCows = 'cow'
    else:
        wordCows = 'cows'

    if procesingNumber != number:
        print(">>>", find_out_number, "\n",
              len(bulls), wordBulls, len(cows), wordCows,
              "\n", "-"*50)
    else:
        print(">>>", find_out_number, "\n", "Correct, you've guessed the right number")

print('Total number of guesses:', counter, "\n", "-"*50)

# hodnoceni
if counter <= 10:
    attempt(0, counter, 10, 'amazing')
elif counter <= 20:
    attempt(10, counter, 20, 'average')
else:
    attempt(20, counter, math.inf, 'not so good')




