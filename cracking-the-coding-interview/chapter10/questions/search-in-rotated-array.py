# assume atleast two elements are inorder

arr = [70, 75, 17, 18, 30, 31, 35, 50, 60]
#arr = [24, 25, 26, 27, 30, 31, 13, 18, 23]


print(arr)


def search(arr, start, end, target):
    if start > end:
        return -1

    mid = round((start+end)/2)
    if arr[mid] == target:
        return mid

    if arr[start] <= arr[mid]:
        if target >= arr[start] and target <= arr[mid]:
            return search(arr, start, mid-1, target)
        return search(arr, mid + 1, end, target)

    if target >= arr[mid] and target <= arr[end]:
        return search(arr, mid + 1, end, target)
    return search(arr, start, mid-1, target)


print(search(arr, 0, len(arr)-1, 17))
