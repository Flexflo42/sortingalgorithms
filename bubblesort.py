# list definition
intList = [4, 12, 102, 44, 2, 98, 67, 42]
n = len(intList)

def bubblesort(intList):
    for i in range(n):    # iterate trough complete list, increment by 1 each time
        for j in range(n-i-1):     # iterate trough 'rest of list' in each iteration (n starts at 1 thats why '-1')
            if intList[j] > intList[j+1]:  
                intList[j], intList[j+1] = intList[j+1], intList[j]    # swap places if element is bigger then the next one
    return intList

sortedList = bubblesort(intList)
print(sortedList)
