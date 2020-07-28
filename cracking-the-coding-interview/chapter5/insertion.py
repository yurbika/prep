def insert(n, m, i, j):
    mask = '1'*abs(j-i) + '0'*i
    mask = ~(int(mask, base=2))
    n &= mask
    n += (m << i)
    return n


print(insert(111, 19, 2, 7))
