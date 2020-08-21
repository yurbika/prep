class Solution:
    def _climbStairs(self, n, memo):
        if n < 0:
            return 0
        if n == 0:
            return 1

        if memo[n] > 0:
            return memo[n]
        else:
            memo[n] = self._climbStairs(
                n-1, memo) + self._climbStairs(n-2, memo)
            return memo[n]

    def climbStairs(self, n: int) -> int:
        return self._climbStairs(n, [0]*(n+1))
