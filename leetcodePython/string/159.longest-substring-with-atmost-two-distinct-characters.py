class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
            if len(s) <= 2:
                return len(s)
            i = 0
            j = 0
            cnt = 0
            solution = ''
            length = 0
            while j < len(s):
                if s[j] not in solution and cnt != 2:
                    solution += s[j]
                    j += 1
                    cnt += 1
                elif s[j] in solution:
                    solution += s[j]
                    j += 1
                else:
                    if len(solution) > length:
                        length = len(solution)
                    i = j-1
                    while i != 0 and s[i-1] == s[i]:
                        i -= 1
                    j = i
                    solution = ''
                    cnt = 0
            if len(solution) > length:
                length = len(solution)
            return length