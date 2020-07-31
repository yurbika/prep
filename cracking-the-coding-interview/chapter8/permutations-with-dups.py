def createPermutations(array, val):
    temp = []
    if len(array) > 1:
        for ele in array:
            for i in range(len(ele)+1):
                if i == 0 and (val+ele) not in temp:
                    temp.append(val + ele)
                elif i == len(ele) and (val+ele) not in temp:
                    temp.append(ele + val)
                elif (ele[:i] + val + ele[i:]) not in temp:
                    temp.append(ele[:i] + val + ele[i:])
    else:
        for i in range(len(array[0])+1):
            if i == 0 and (val+array[0]) not in temp:
                temp.append(val + array[0])
            elif i == len(array[0]) and (array[0]+val) not in temp:
                temp.append(array[0] + val)
            elif ((array[0])[:i] + val + (array[0])[i:]) not in temp:
                temp.append((array[0])[:i] + val + (array[0])[i:])
    return temp


def permutation(s, memo):
    if len(s) == 2:
        memo += createPermutations([s[0]], s[1])
        return memo

    memo = createPermutations(permutation(s[:-1], memo), s[-1])
    return memo


print(permutation('aab', []))
print(permutation('acccdab', []))
