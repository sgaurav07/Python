#BubbleSort 
i,j,l,k = 0,0,0,0
def bubbleSort(arr):
    l = len(arr)
    for i in range(l):
        for j in range(0,l-i-1):
            if arr[j] < arr[j+1]:
                arr[j],arr[j+1]= arr[j+1], arr[j]
    
    return arr


#Selection Sort Algorithm

def selectionSort(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range(i+1,len(arr)):
            if arr[minIndex] > arr[j]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex],arr[i]

    return arr

#Recursive Bubble Sort

def recursiveBubbleSort(arr):
    for i, num in enumerate(arr):
        try:
            if arr[i+1] < num:
                arr[i], arr[i+1] = arr[i+1], num
                recursiveBubbleSort(arr)
        except IndexError:
            pass
    return arr


#Insertion Sort

def insertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr

#Merge Sort

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2 
        Left = arr[:mid]
        Right = arr[mid:]
        mergeSort(Left)
        mergeSort(Right)
        i = j  = k = 0

        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                arr[k] = Left[i]
                i += 1
            else:
                arr[k] = Right[j]
                j += 1
            k +=1

        while i < len(Left):
            arr[k] = Left[i]
            i+=1
            k+=1
        
        while j < len(Right):
            arr[k] = Right[j]
            j+=1
            k+=1
    
    return arr

#Print List Function
def printArray(arrToPrint):
    for i in range(0,len(arrToPrint)):
        if i != len(arrToPrint):
            print(arrToPrint[i], end = " ")
        else:
            print(arrToPrint[i])