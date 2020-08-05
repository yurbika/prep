import random

arr1 = [random.randint(-10, 15) for ele in range(10)]
arr2 = [random.randint(-10, 15) for ele in range(5)]
arr1.sort()
arr2.sort()

arr1 = arr1 + [0 for i in range(len(arr2))]
print(arr1)
print(arr2)


def mergeTwoList(arr1, arr2):
    indexMerged = len(arr1)-1-len(arr2)+len(arr2)
    i = arr1.index(max(arr1))
    j = len(arr2) - 1
    while j >= 0:
        if i >= 0 and arr1[i] > arr2[j]:
            arr1[indexMerged] = arr1[i]
            i -= 1
        else:
            arr1[indexMerged] = arr2[j]
            j -= 1

        indexMerged -= 1

    return arr1


print(mergeTwoList(arr1, arr2))
