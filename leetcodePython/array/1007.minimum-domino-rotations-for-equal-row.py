class Solution:
    def swaps(self, target, a, b):
        cnt = 0
        for i in range(len(a)):
            if a[i] != target and b[i] != target:
                return sys.maxsize
            elif a[i] != target:
                cnt += 1
        return cnt

    def minDominoRotations(self, a: List[int], b: List[int]) -> int:
        cnt = min(self.swaps(a[0], a, b), self.swaps(b[0], a, b))
        cnt = min(cnt, self.swaps(a[0], b, a))
        cnt = min(cnt, self.swaps(b[0], b, a))

        if cnt != sys.maxsize:
            return cnt
        else:
            return -1
