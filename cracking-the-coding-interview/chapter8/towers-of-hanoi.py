arr = [
    [1, 2, 3],
    [],
    []]


def moveToDestintaion(value, destination):
    destination.insert(0, value)


def solve(length, origin, buffer, destination):
    if length > 0:
        solve(length-1, origin, destination, buffer)
        moveToDestintaion(origin.pop(0), destination)
        solve(length-1, buffer, origin, destination)


print(solve(len(arr[0]), arr[0], arr[1], arr[2]))
