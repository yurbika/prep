class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        if len(M) == 0:
            return 0
        dp = [[[0, 0, 0, 0] for j in range(len(M[0]))] for i in range(len(M))]
        res = 0

        for i in range(len(M)):
            for j in range(len(M[i])):
                if M[i][j]:
                    dp[i][j][0] = dp[i][j-1][0] + 1 if j > 0 else 1
                    dp[i][j][1] = dp[i-1][j][1]+1 if i > 0 else 1
                    dp[i][j][2] = dp[i-1][j-1][2]+1 if i > 0 and j > 0 else 1
                    dp[i][j][3] = dp[i-1][j+1][3] + \
                        1 if i > 0 and j < len(M[i])-1 else 1
                res = max(res, dp[i][j][0], dp[i][j]
                          [1], dp[i][j][2], dp[i][j][3])

        return res
