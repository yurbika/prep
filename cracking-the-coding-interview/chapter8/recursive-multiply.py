# assume num1 is always greater than num2

def recursiveMultiply(num1, num2, result):
    if num1 == 0 or num2 == 0:
        return 0

    if num1 == 1 or num2 == 1:
        return num1*num2

    if result > (num1 * num2):
        return result >> 1

    if result == (num1 * num2):
        return result

    result = recursiveMultiply(num1, num2, result << 1)
    if result == (num1 * num2):
        return result
    result = recursiveMultiply(num1, num2, result+num1)
    if result == (num1 * num2):
        return result
    result = recursiveMultiply(num1, num2, result-num2)

    return result


num1 = 500
num2 = 5

print(recursiveMultiply(num1, num2, num1))
