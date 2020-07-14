#Given two strings, wirte a method to decide if one is a permuatation of the other

string = "adc"
string2 = "cad"

def sortString(string):
  return sorted(string)

print(sortString(string) == sortString(string2))


#Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string. Also LeetCode Problem ID: 567

s2 = "eidboaooo"
s1 = "ab"

def checkInclusion(s1, s2):
    A = [ord(x) - ord('a') for x in s1]
    B = [ord(x) - ord('a') for x in s2]
    target = [0] * 26
    for x in A:
        target[x] += 1

    window = [0] * 26
    for i, x in enumerate(B):
        window[x] += 1
        if i >= len(A):
            window[B[i - len(A)]] -= 1
        if window == target:
            return True
    return False
   
checkInclusion(s1,s2)