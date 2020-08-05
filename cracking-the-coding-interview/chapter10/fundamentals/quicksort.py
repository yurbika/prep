# best time O(n log n)
# average time O(n log n)
# worst time O(n^2)

# worst space O(log n)


arr = [3, 7, 8, 2, 1]


def partition(arr, left, right):
    pivot = arr[right]

    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1

    arr[i], arr[right] = arr[right], arr[i]
    return i + 1


def quickSort(arr, start, end):
    if start >= end:
        return

    p = partition(arr, start, end)
    quickSort(arr, start, p-1)
    quickSort(arr, p+1, end)


quickSort(arr, 0, len(arr)-1)
print(arr)
