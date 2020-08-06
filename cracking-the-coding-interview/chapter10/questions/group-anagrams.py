arr = ['real fun', 'nag a ram', 'listen', 'school master', "dormitory", 'the classroom',
       'pairs', 'funeral', 'dirty room', 'silent', 'paris', 'anagram']

#   assume that an angram is a string just in different order,
#   which means every character must be in the other string
#   also assume every character is lowercase

print(arr)


def isValid(s1, s2):
    string1 = s1.replace(' ', '')
    string2 = s2.replace(' ', '')
    string1 = set(string1)
    string2 = set(string2)

    if len(string1.intersection(string2)) == len(string1):
        return True
    else:
        return False


def sortAnagrams(arr):
    lastPos = 0
    for i in range(len(arr)):
        if lastPos >= len(arr)-1:
            break
        i = lastPos
        lastPos = i+1
        for j in range(i+1, len(arr)):
            if isValid(arr[i], arr[j]):
                arr[lastPos], arr[j] = arr[j], arr[lastPos]
                lastPos += 1

    return arr


print(sortAnagrams(arr))
