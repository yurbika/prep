n = 50


def coins(n, penny, currentArr, memo):
    if n == 0:
        if penny == 1:
            currentArr[0] += 1
        elif penny == 5:
            currentArr[1] += 1
        elif penny == 10:
            currentArr[2] += 1
        elif penny == 25:
            currentArr[3] += 1
        if currentArr not in memo:
            memo.append(currentArr[:])
            return memo, currentArr
        else:
            return memo, currentArr

    if n < -1:
        n += penny
        if penny == 1:
            currentArr[0] -= 1
        elif penny == 5:
            currentArr[1] -= 1
        elif penny == 10:
            currentArr[2] -= 1
        elif penny == 25:
            currentArr[3] -= 1
        return memo, currentArr

    if penny == 1:
        currentArr[0] += 1
    elif penny == 5:
        currentArr[1] += 1
    elif penny == 10:
        currentArr[2] += 1
    elif penny == 25:
        currentArr[3] += 1

    if n >= 25:
        memo, currentArr = coins(n-25, 25, currentArr, memo)
        if currentArr[3] > 0:
            currentArr[3] -= 1

    if n >= 10:
        memo, currentArr = coins(n-10, 10, currentArr, memo)
        if currentArr[2] > 0:
            currentArr[2] -= 1

    if n >= 5:
        memo, currentArr = coins(n-5, 5, currentArr, memo)
        if currentArr[1] > 0:
            currentArr[1] -= 1

    if n >= 1:
        memo, currentArr = coins(n-1, 1, currentArr, memo)
        if currentArr[0] > 0:
            currentArr[0] -= 1
    return memo, currentArr


arr = coins(n, 0, [0]*4, [])[0]
print(arr, "\n", len(arr))
