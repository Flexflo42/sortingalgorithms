import time

intList = [3, 7, 21, 9, 4, 12, 102, 44, 2, 98, 67, 42]
aMiracleHappened = [2, 3, 4]

def miracleSort(intList):
    while True:
        if all(intList[i] <= intList[i+1] for i in range(len(intList)-1)):
            print("The List is sorted")
            exit()
        else:
            print("The List is not sorted. We should wait for divine intervention")
            time.sleep(2)

miracleSort(aMiracleHappened)

