class Solution:
    def expressiveWords(self, s, words):
        if s == "":
            return 0
        cnt = 0
        for w in words:
            p1 = 0
            p2 = 0
            if s[p1] != w[p2] and w == '':
                continue
            else:
                while p1 < len(s):
                    if p2 < len(w) and s[p1] == w[p2]:
                        p2 += 1
                    # elif s[p1 - 1:p1 + 2] != s[p1] * 3 and s[p1]* 3 != s[p1 - 2:p1 + 1]:
                    elif s[p1 - 1:p1 + 2] != s[p1] * 3 != s[p1 - 2:p1 + 1]:
                        break
                    p1 += 1
                if p1 >= len(s) and p2 >= len(w):
                    cnt += 1

        return cnt
