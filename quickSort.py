def QuickSort(A, low, high):
    if (low < high):
        j = partition(A, low, high)
        QuickSort(A, low, j)
        QuickSort(A, j + 1, high)


def partition(A, low, high):
    pivot = A[low]
    i = low
    j = high

    while (i < j):
        while (A[i] <= pivot):
            i = i + 1

        while (A[j] > pivot):
            j = j - 1

        if (i < j):
            temp = A[i]
            A[i] = A[j]
            A[j] = temp

    temp = A[low]
    A[low] = A[j]
    A[j] = temp
    return j;




A=[ 6, 5, 8, 9, 3, 10, 15, 12, 16]
print("Given Array: ",A)
QuickSort(A, 0, len(A)-1)
print("Sorted Array: ",A)
                   ```
