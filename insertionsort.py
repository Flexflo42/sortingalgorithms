# list definition
intList = [4, 12, 102, 44, 2, 98, 67, 42]

"""
Insertion sort has an outer and an inner loop.
The outerloop iterates trough the whole list,
while the inner loop iterates trough a sublist.
In the inner loop the smallest element gets found
and swapped to the current position of the outer loop.
This way the list gets sorted ascending.
Runtime can be estimated by O(n²)
"""

def insertionsort(intList):
    n = len(intList)
    for i in range(n):
        smallestElement = i
        for j in range(i+1, n):    # start comparing following elements with the 'first' of current iteration
            if intList[j] < intList[smallestElement]:    # comparing to concrete Values
                smallestElement = j    # saving the index of new smallest
        print(f"swapping {intList[i]} with {intList[smallestElement]}")    # debuging print statement, can be removed if wanted
        intList[i], intList[smallestElement] = intList[smallestElement], intList[i]    # swapping index i with smallest element 
    return intList

sortedList = insertionsort(intList)
print(sortedList)

