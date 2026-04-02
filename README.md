# sortingalgorithms
Implementing standard and not so standard sorting algorithms for practice.

## Miracle Sort
Sorting algorithm based on the idea of waiting till something happens. When you wait enough everything will always sort itself. Needs strong faith and lucky Bitflips on RAM that doesnt automatically corrects errors. 

## Bogosort
Unstable sorting algorithm that randomizes the indexes of elements till the input is sorted. Every list has n! permutations so the chance for success in a single execution of the algorithm is 1/n!. The chance for one success in k amount of algorithm runs is 1 - (1 - 1/n!)^k where k is the amount of runs. 
