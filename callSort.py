# Sorting Algorithm Calling in Python

import SortingLibrary as sl

arr = [34,99,54,10,22,8,1,12]
print("Before Selection Sort")
sl.printArray(arr)

print("\nAfter Selection Sort")
sortedArr = sl.selectionSort(arr) # or sl.selectionSort(arr) return value is same
sl.printArray(sortedArr)