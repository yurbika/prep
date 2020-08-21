class Solution:
    def balancedStringSplit(self, s: str) -> int:
        rCnt = 0
        lCnt = 0
        solution = 0
        for i in s:

            if i == 'R':
                rCnt += 1
            else:
                lCnt += 1

            if rCnt == lCnt:
                solution += 1
                rCnt = 0
                lCnt = 0

        return solution
