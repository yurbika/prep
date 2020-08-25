class Solution:
    def recursion(self, i, s, memo):
        if i == len(s):
            return 1

        if s[i] == '0':
            return 0

        if i == len(s)-1:
            return 1

        if memo[i]:
            return memo[i]
        else:
            memo[i] = self.recursion(
                i+1, s, memo) + (self.recursion(i+2, s, memo) if int(s[i:i+2]) <= 26 else 0)
            return memo[i]

    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        memo = [0 for i in range(len(s))]
        return self.recursion(0, s, memo)
