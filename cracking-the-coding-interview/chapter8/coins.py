n = 27

# recursion with list of variations


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

# dynamic programming version


def dpCoins(coins, coinsArrLength, total):
    arr = [[0 for i in range(coinsArrLength)] for j in range(total+1)]
    x = 0
    y = 0

    for i in range(coinsArrLength):
        arr[0][i] = 1

    for i in range(1, total+1):
        for j in range(coinsArrLength):

            if i - coins[j] >= 0:
                y = arr[i - coins[j]][j]
            else:
                y = 0

            if j >= 1:
                x = arr[i][j-1]
            else:
                x = 0

            arr[i][j] = x + y

    return arr[total][coinsArrLength-1]


arr = [1, 5, 10, 25]
arrLength = len(arr)
print(dpCoins(arr, arrLength, 100))

# only recursion version


def recursionCoins(coins, coinsArrLength, n):
    if n == 0:
        return 1

    if n < 0:
        return 0

    if coinsArrLength <= 0 and n >= 1:
        return 0

    return recursionCoins(coins, coinsArrLength-1, n) + \
        recursionCoins(coins, coinsArrLength, n-coins[coinsArrLength-1])


print(recursionCoins(arr, arrLength, 27))
