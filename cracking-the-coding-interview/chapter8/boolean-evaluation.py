a = '0&0&0&1^1|0'


def stringToBoolean(c):
    if c == '1':
        return True
    else:
        return False


def evaluation(string, result):
    if len(string) == 0:
        return 0

    if len(string) == 1:
        if stringToBoolean(string) == result:
            return 1
        else:
            return 0

    ways = 0
    for i in range(1, len(string), 2):
        c = string[i]
        left = string[0:i]
        right = string[i+1:]

        leftTrue = evaluation(left, True)
        leftFalse = evaluation(left, False)
        rightTrue = evaluation(right, True)
        rightFalse = evaluation(right, False)
        total = (leftTrue+leftFalse) * (rightTrue+rightFalse)

        totalTrue = 0
        if c == '^':
            totalTrue = leftTrue * rightFalse + leftFalse * rightTrue
        elif c == '&':
            totalTrue = leftTrue * rightTrue
        elif c == '|':
            totalTrue = leftTrue * rightTrue + leftFalse * rightTrue + leftTrue * rightFalse

        if result:
            subWays = totalTrue
        else:
            subWays = total - totalTrue

        ways += subWays

    return ways


print(evaluation(a, True))
