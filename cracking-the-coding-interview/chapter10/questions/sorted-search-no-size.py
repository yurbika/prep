import random
arr = [random.randint(0, 1564998) for i in range(548987)]
arr.sort()


def elementAt(arr, i):
    try:
        return arr[i]
    except IndexError:
        return -1


def startSearch(arr, target):
    index = 1

    while elementAt(arr, index) < target and elementAt(arr, index) != -1:
        index *= 2

    return search(arr, index/2, index, target)


def search(arr, start, end, target):
    if end < start or end == start and arr[start] != target:
        return False

    if end == start and arr[start] == target:
        return True

    midPos = round((start+end)/2)
    midValue = arr[midPos]

    if midValue == target:
        return True

    if midValue > target:
        return search(arr, start, midPos-1, target)
    else:
        return search(arr, midPos+1, end, target)


print(startSearch(arr, 14))
