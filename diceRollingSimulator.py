print("**** Dice Rolling Simulator ****")

import random
MIN = 1
MAX = 6

def diceRollingSimulator():
    print("Dice Roll Start!")
    ans = 'Y'
    while ans != 'N':
        print("The number is : ", random.randint(MIN, MAX))
        ans = input("Would you like to roll again? (Y/N) : ")
    print("Dice Roll Stop!")

diceRollingSimulator()