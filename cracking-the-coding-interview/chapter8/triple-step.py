n = 15

# only recursion


def step(n):
    if n < 0:
        return 0

    if n == 0:
        return 1

    return step(n-1) + step(n-2) + step(n - 3)


print(step(n))


def stepM(n, memo):
    if n < 0:
        return 0

    if n == 0:
        return 1

    if memo[n] > 0:
        return memo[n]

    else:
        memo[n] = stepM(n-1, memo) + stepM(n-2, memo) + stepM(n - 3, memo)
        return memo[n]


print(stepM(n, [0]*(n+1)))
