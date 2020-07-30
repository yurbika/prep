import random


def createArr():
    arr = []
    while len(arr) < 70:
        arr.append(random.randint(-15, 50))

    arr = list(set(arr))
    arr.sort()
    return arr


def findIndex(arr, start, end):
    if not arr:
        return

    if end == start and arr[end] == end:
        return end

    if start >= len(arr)-1 or end <= 0 or end < start or end == start:
        return

    midPos = round((len(arr[start:end])-1)/2)
    midValue = (arr[start:end])[midPos]
    # get the real index
    midPos = arr.index(midValue)

    if midValue == midPos:
        return midPos

    if midValue < midPos:
        return findIndex(arr, midPos+1, len(arr)-1)
    else:
        return findIndex(arr, start, midPos-1)


arr = createArr()
print(findIndex(arr, 0, len(arr)))

arr = createArr()
print(findIndex(arr, 0, len(arr)))

arr = createArr()
print(findIndex(arr, 0, len(arr)))

arr = createArr()
print(findIndex(arr, 0, len(arr)))

arr = createArr()
print(findIndex(arr, 0, len(arr)))

arr = createArr()
print(findIndex(arr, 0, len(arr)))

arr = createArr()
print(findIndex(arr, 0, len(arr)))

arr = createArr()
print(findIndex(arr, 0, len(arr)))

arr = createArr()
print(findIndex(arr, 0, len(arr)))

arr = createArr()
print(findIndex(arr, 0, len(arr)))

arr = createArr()
print(findIndex(arr, 0, len(arr)))

arr = createArr()
print(findIndex(arr, 0, len(arr)))

arr = createArr()
print(findIndex(arr, 0, len(arr)))

arr = createArr()
print(findIndex(arr, 0, len(arr)))

arr = createArr()
print(findIndex(arr, 0, len(arr)))

arr = createArr()
print(findIndex(arr, 0, len(arr)))
