class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        if len(s) == 1:
            return 1

        i = 0
        j = 0
        solution = 0
        temp = ''

        while i < len(s) and j < len(s):
            if s[j] not in temp:
                temp += s[j]
                j += 1
            else:
                while s[j] in s[i:j] and i < j:
                    i += 1
                j += 1
                temp = s[i:j]
            if len(s[i:j]) > solution:
                solution = len(s[i:j])

        return solution
