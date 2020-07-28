# 1010101010 => 682
# 0101010101 => 341

def swap(num):
    even = ''
    odd = ''
    solution = ''

    while num != 0:
        even = f'{num & 1}' + even
        num = num >> 1
        odd = f'{num & 1}' + odd
        num = num >> 1

    while odd:
        solution = odd[-1] + solution
        odd = odd[:len(odd)-1]
        solution = even[-1] + solution
        even = even[:len(even)-1]

    return int(solution, base=2)


print(swap(10))


def rshift(val, n): return (val % 0x100000000) >> n


def test(n):
    # save all the odd numbers with 101010 same with even 010101
    # do it in 32 bits
    # found out 2863311530 is 0xaaaaaaaa
    # and 1431655765 is 0x55555555
    return (rshift(n & 2863311530, 1) | ((n & 1431655765) << 1))


print(test(37))
