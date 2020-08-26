class Solution(object):
    def countCornerRectangles(self, grid):
        dp = []
        ans = 0
        for row in grid:
            posOfOnes = {idx for idx, val in enumerate(row) if val}
            for prevPosOfOnes in dp:
                matches = len(posOfOnes & prevPosOfOnes)
                ans += matches * (matches-1) // 2
            dp.append(posOfOnes)

        return ans
