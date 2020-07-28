def binaryToString(num):
    if num > 1 or num < 0:
        print('error')
        return
    s = '0.'
    while len(s) <= 32:
        num *= 2.0
        if num == 1:
            s += '1'
            print(s)
            return
        if num > 1:
            s += '1'
            num -= 1.0
        else:
            s += '0'

    print('error')


binaryToString(0.0625)
