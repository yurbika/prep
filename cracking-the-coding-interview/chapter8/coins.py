n = 27


def coins(n, penny, currentArr, memo):
    if n == 0:
        if penny != 0:
            if penny == 1:
                currentArr[0] += 1
            if penny == 5:
                currentArr[1] += 1
            if penny == 10:
                currentArr[2] += 1
            if penny == 25:
                currentArr[3] += 1
        temp = currentArr[:]
        if temp not in memo:
            memo.append(temp)
        return memo

    if n < 0:
        n += penny
        return memo

    if penny != 0:
        if penny == 1:
            currentArr[0] += 1
        if penny == 5:
            currentArr[1] += 1
        if penny == 10:
            currentArr[2] += 1
        if penny == 25:
            currentArr[3] += 1

    memo = coins(n-1, 1, currentArr, memo)
    if currentArr[0] > 0:
        currentArr[0] -= 1

    memo = coins(n-5, 5, currentArr, memo)
    if currentArr[1] > 0 and (n-5) <= 0:
        currentArr[1] -= 1

    memo = coins(n-10, 10, currentArr, memo)
    if currentArr[2] > 0 and (n-10) <= 0:
        currentArr[2] -= 1

    memo = coins(n-25, 25, currentArr, memo)
    if currentArr[3] > 0 and (n-25) <= 0:
        currentArr[3] -= 1

    return memo


arr = coins(n, 0, [0]*4, [])
print(arr, "\n", len(arr))
