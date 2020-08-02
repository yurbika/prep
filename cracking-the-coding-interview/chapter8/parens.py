def parens(left, right, string, result):
    if left == 0 and right == 0:
        result.append(string)
        return

    if left > 0:
        parens(left-1, right, string+'(', result)

    if right > left:
        parens(left, right-1, string+')', result)


arr = []
n = 3

parens(n, n, '', arr)

for i in arr:
    print(i)
