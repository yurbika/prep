class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        if s == '' or len(s) < 3:
            return

        l = 0
        r = 1
        solution = []

        while r < len(s):
            if s[l] != s[r] and r - l >= 3:
                solution.append([l, r-1])
                l = r
            elif s[l] != s[r]:
                l = r
            else:
                r += 1

        if s[l] == s[r-1] and r - l >= 3:
            solution.append([l, r-1])
        return solution
