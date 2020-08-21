class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        c = math.ceil(len(B) / len(A))
        s = A*c
        if B in s:
            return c
        elif B in s+A:
            return c+1
        else:
            return -1
