print("**** Guess The Number ****")

import random
MIN = 1
MAX = 100

def guessTheNumber(MIN, MAX):
    guess = random.randint(MIN, MAX)
    nb = int(input("Entrer le nombre mystere : "))
    while nb != guess:
        if nb > guess:
            print("C'est moins !")
            nb = int(input("Entrer le nombre mystere : "))
        elif nb < guess:
            print("C'est plus !")
            nb = int(input("Entrer le nombre mystere : "))
    print("Bravo! Le nombre mystere est ", guess)
    

guessTheNumber(MIN, MAX)