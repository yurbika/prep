arr = ['a', '', '', '', 'alkösjd', '', '', '', '', '', 'baödöa', '', '', '', '', '', '', '', 'caslökdjf', '',
       '', '', 'daaa', '', 'dad', 'qpwe', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'ssssss', '', '', '', '', '', '', 'test']

print(arr[0] > arr[4])


def search(arr, start, end, target, bigger):
    if start > end or start == end and arr[start] != target:
        return

    if start == end and arr[start] == target:
        return arr.index(target)

    midPos = round((start+end)/2)
    while arr[midPos] == '':
        if bigger:
            midPos -= 1
        else:
            midPos += 1
    midValue = arr[midPos]

    if midValue == target:
        return arr.index(target)

    if midValue > target:
        return search(arr, start, midPos-1, target, True)
    else:
        return search(arr, midPos+1, end, target, False)


print(search(arr, 0, len(arr)-1, 'dad', False))
