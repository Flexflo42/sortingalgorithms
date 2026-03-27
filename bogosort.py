import random
import math
import time

# good luck
intList = [4, 12, 102, 44, 2, 98, 67, 42]
n = len(intList)

def calculateChance(k):
    k = int(k)
    x = len(intList)
    factorial = math.factorial(x)
    chance = 1 - (1 - x/factorial)**k
    return chance

def bogosort(intList):
    attempts = 0
    while True:
        if all(intList[i] <= intList[i+1] for i in range(len(intList)-1)):
            print("The List is sorted")
            return intList, attempts
        random.shuffle(intList)
        attempts += 1
        print(f"Everday I'm shuffling #{attempts}: {intList}")

userGuess = input(f"How many attempts do you think will a list with {n} Elements take? : ")
chance = calculateChance(userGuess)
print(f"the chance of this being a success is {chance}")
time.sleep(10)
print("LETS ROLL")

sorted_list, attempts = bogosort(intList)