s = "abc"


def createPermutations(array, val):
    temp = []
    if len(array) > 1:
        for ele in array:
            for i in range(len(ele)+1):
                if i == 0:
                    temp.append(val + ele)
                elif i == len(ele):
                    temp.append(ele + val)
                else:
                    temp.append(ele[:i] + val + ele[i:])
    else:
        for i in range(len(array[0])+1):
            if i == 0:
                temp.append(val + array[0])
            elif i == len(array[0]):
                temp.append(array[0] + val)
            else:
                temp.append((array[0])[:i] + val + (array[0])[i:])
    return temp


createPermutations(createPermutations(["a"], 'b'), 'c')


def permutation(s, memo):
    if len(s) == 2:
        memo += createPermutations([s[0]], s[1])
        return memo

    memo = createPermutations(permutation(s[:-1], memo), s[-1])
    return memo


print(permutation('abc', []))
