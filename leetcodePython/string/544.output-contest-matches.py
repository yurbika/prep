class Solution:
    def findContestMatch(self, n: int) -> str:
        res = list(range(1, n + 1))
        while len(res) > 1:
            res = [f'({res[i]},{res[-i-1]})' for i in range(round(len(res)/2))]
        return res[0]
