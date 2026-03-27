import random

intList = [21, 9, 4, 12, 102, 44, 2, 98, 67, 42]
#

def bogosort(intList):
    while True:
        if all(intList[i] <= intList[i+1] for i in range(len(intList)-1)):
            print("The List is sorted")
            return intList
        random.shuffle(intList)
        print("Everday I'm shuffling")

bogosort(intList)