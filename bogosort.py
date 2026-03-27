import random

# good luck
intList = [4, 12, 102, 44, 2, 98, 67, 42]

def bogosort(intList):
    attempts = 0
    while True:
        if all(intList[i] <= intList[i+1] for i in range(len(intList)-1)):
            print("The List is sorted")
            return intList
        random.shuffle(intList)
        attempts += 1
        print(f"Everday I'm shuffling #{attempts}: {intList}")

bogosort(intList)