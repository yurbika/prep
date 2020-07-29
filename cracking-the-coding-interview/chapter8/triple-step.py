n = 15

# only recursion


def step(n):
    if n < 0:
        return 0

    if n == 0:
        return 1

    return step(n-1) + step(n-2) + step(n - 3)


print(step(n))
