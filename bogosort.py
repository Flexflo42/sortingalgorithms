import random
import math
import time

# list definition
intList = [4, 12, 102, 44, 2, 98, 67, 42]
n = len(intList)

# function that calculates the chance of success within a number of attempts, given by the user
def calculateChance(k, n):
    k = int(k)
    factorial = math.factorial(n)
    chance = 1 - (1 - 1/factorial)**k
    return chance

# algorithm that randomizes the elements in a list till they are sorted
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
chance = calculateChance(userGuess, n)
print(f"the chance of this being a success is {chance}")
time.sleep(1)
print("LETS ROLL")

sorted_list, attempts = bogosort(intList)