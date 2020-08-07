def sort(arr):
    peak = True
    for i in range(1, len(arr)):
        if peak:
            index = arr.index(max(arr[i-1:]))
            arr[i-1], arr[index] = arr[index], arr[i-1]
            peak = False
        else:
            peak = True
            index = arr.index(min(arr[i-1:]))
            arr[i-1], arr[index] = arr[index], arr[i-1]

    return arr


arr = [9, 1, 1, 0, 5, 3, 3, 4, 8, 7]

print(sort(arr))
