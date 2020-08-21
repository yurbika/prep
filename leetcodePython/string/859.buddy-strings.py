class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if A == '' or B == '':
            return False
        if A == B and len(set(A)) < len(A):
            return True
        elif A == B and len(set(A)) >= len(A):
            return False
        if len(A) != len(B):
            return False

        cnt = 0
        for i in range(len(B)):
            if A.count(B[i]) != B.count(B[i]):
                return False
            if A[i] != B[i]:
                cnt += 1
            if cnt > 2:
                return False

        return True
