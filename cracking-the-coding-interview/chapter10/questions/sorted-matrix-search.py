import math
# every row is sorted
# also every column is sorted
arr1 = [
    [15, 20,  70,  85,  90],
    [20, 35,  80,  95, 100],
    [30, 55,  95, 110, 111],
    [40, 80, 111, 120, 135]
]


# every row is sorted and the first number in the next row is >= to the last item in the row before
arr2 = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11]
]

# we are mapping the 2d array to an 1d array with
# row equals to floor((startValue + endValue)/2/len(arr[0]))
# col equals to floor((startValue + endValue)/2%len(arr[0]))


def searchForArr2(arr, start, end, target):
    if start > end or start == end and arr[math.floor(((start+end)/2)/len(arr[0]))][math.floor((start+end)/2 % len(arr[0]))] != target:
        return

    if start == end and arr[math.floor(((start+end)/2)/len(arr[0]))][math.floor((start+end)/2 % len(arr[0]))] == target:
        return [math.floor(((start+end)/2)/len(arr[0])),
                math.floor((start+end)/2 % len(arr[0]))]

    midPos = [math.floor(((start+end)/2)/len(arr[0])),
              math.floor((start+end)/2 % len(arr[0]))]
    midValue = arr[midPos[0]][midPos[1]]

    if midValue == target:
        return midPos

    if midValue > target:
        if midPos[1] == 0:
            return searchForArr2(arr, start, arr[midPos[0]-1][-1], target)
        else:
            return searchForArr2(arr, start, arr[midPos[0]][midPos[1]-1], target)
    else:
        if midPos[1] == len(arr[0])-1:
            return searchForArr2(arr, arr[midPos[0]+1][0], end, target)
        else:
            return searchForArr2(arr, arr[midPos[0]][midPos[1]+1], end, target)


print(searchForArr2(arr2, arr2[0][0], arr2[-1][-1], 4))
