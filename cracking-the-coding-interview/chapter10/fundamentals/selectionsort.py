import random

arr = [random.randint(-50, 10) for ele in range(25)]

print(arr)


def selectionSort(arr):
    for i in range(len(arr)):
        minValue = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minValue]:
                minValue = j

        if minValue != i:
            arr[i], arr[minValue] = arr[minValue], arr[i]

    return arr


print(selectionSort(arr))
