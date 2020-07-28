import math
import sys

num = 1775  # 11011101111
#output: 8

# solution 1 with O(n) space


def flip(num):
    if num == 0:
        return 1

    if int(bin(~num).split('0b1')[1], base=2) == 0:
        print(num)
        return len(bin(num).split('0b')[1])

    s = [i for i in (bin(num).split('0b')[1])]

    solution = 0
    i = 0
    lastI = 0
    while True:
        cnt = 0
        try:
            i = s.index('0', i)
        except ValueError:
            break
        s[i] = '1'
        for x in range(lastI, len(s)):
            if s[x] == '1':
                cnt += 1
            else:
                break
        if cnt > solution:
            solution = cnt
        s[i] = 0
        i += 1
        lastI = i

    return solution


print(flip(sys.maxsize))
print("\n")
print(flip(round(math.exp(500))))

# solution 2 with O(1) space


def shiftToWin(num):
    if num == 0:
        return 1

    if int(bin(~num).split('0b1')[1], base=2) == 0:
        print(num)
        return len(bin(num).split('0b')[1])

    cnt = 0
    currBit = 0
    flipped = False
    solution = 0
    while num:
        currBit = num & 1
        num = num >> 1

        if currBit == 1:
            cnt += 1
        elif currBit == 0 and not flipped:
            cnt += 1
            flipped = True
        else:
            flipped = False
            if cnt > solution:
                solution = cnt
            cnt = 1
        if cnt > solution:
            solution = cnt
    return solution


print("\n")
print(shiftToWin(sys.maxsize))
