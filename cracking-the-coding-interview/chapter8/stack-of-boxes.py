import random

arr = [(random.randrange(1, 20), random.randrange(
    1, 20), random.randrange(1, 20)) for i in range(100)]

# arr = [(3, 4, 5), (1, 3, 4), (2, 4, 5), (25, 13, 62), (1, 3, 4), (12, 7, 50)]

for i in arr:
    print(i)

# backtracking solution
# assume no box has a zero value


def isValid(box, solution):
    box1 = solution[-1]
    for i in range(len(box)):
        if box1[i] < box[i]:
            return False
    return True


def stack(arr, heightSum, solutionSum, solutionArr):
    if not arr and heightSum > solutionSum:
        solutionSum = heightSum
        return solutionSum

    for i in range(len(arr)):
        box = arr[i]
        if not solutionArr or isValid(box, solutionArr):
            solutionArr.append(box)
            heightSum += box[1]
            temp = arr[:arr.index(box)] + arr[arr.index(box)+1:]
            solutionSum = stack(temp, heightSum,
                                solutionSum, solutionArr)
            if heightSum > solutionSum:
                solutionSum = heightSum
            heightSum -= box[1]
            solutionArr.pop()
    return solutionSum


print(stack(arr, 0, 0, []))
