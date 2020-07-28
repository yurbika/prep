# 22 => 10110
# 25 => 11001
# 26 => 11010

# 1135 => 10001101111
# 1143 => 10001110111
# 1147 => 10001111011

def nextN(num):
    binArr = bin(num).split('0b')[1]
    binArrOneCnt = binArr.count('1')
    ln = 0
    sn = 0
    temp = num

    while True:
        temp += 1
        if (bin(temp).split('0b')[1]).count('1') == binArrOneCnt:
            ln = temp
            break

    temp = num

    while True:
        temp -= 1
        if (bin(temp).split('0b')[1]).count('1') == binArrOneCnt:
            sn = temp
            break

    return f'{ln}, {num}, {sn}'


print(nextN(13948))

#93786, 93785, 93782
# 101101110010 10110
# 101101110010 11001
# 101101110010 11010

# 640 576 544
# 1010000000
# 1001000000
# 1000100000
