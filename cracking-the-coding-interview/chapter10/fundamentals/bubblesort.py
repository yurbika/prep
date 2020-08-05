import random
arr = [random.randint(-50, 10) for ele in range(25)]

print(arr)


def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


print(bubbleSort(arr))
