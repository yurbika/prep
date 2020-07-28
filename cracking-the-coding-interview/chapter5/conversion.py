# input: 11101 => 29
# target: 01111 => 15
# output: 2

def conversion(num1, num2):
    if num1 == num2:
        return 0

    temp = num1 ^ num2
    return bin(temp).split('0b')[1].count('1')


print(conversion(29, 15))


# her solution
def conversion2(num1, num2):
    if num1 == num2:
        return 0

    temp = num1 ^ num2
    cnt = 0
    while temp != 0:
        temp = temp & (temp-1)
        cnt += 1
    return cnt


print(conversion2(29, 15))
