# best/average/worst time O(n log n)
# worst space O(n)
import random


arr = [random.randint(-50, 150) for ele in range(25)]

print(arr)


def sort(arr1, arr2):
    temp = []
    i = 0
    j = 0
    while (i+j) < len(arr1 + arr2):
        if i < len(arr1) and arr1[i] < arr2[j]:
            temp.append(arr1[i])
            i += 1

        elif j < len(arr2) and arr2[j] < arr1[i]:
            temp.append(arr2[j])
            j += 1

        if i == len(arr1):
            temp += arr2[j:]
            break
        if j == len(arr2):
            temp += arr1[i:]
            break

    return temp


def mergeSort(arr):
    if len(arr) == 0:
        return arr

    if len(arr) == 1:
        return arr

    left = mergeSort(arr[:round(len(arr)/2)])
    right = mergeSort(arr[round(len(arr)/2):])
    arr = sort(left, right)

    return arr


print(mergeSort(arr))
