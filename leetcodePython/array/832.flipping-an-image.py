#my solution

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        if len(A) == 0:
            return A
        
        
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] == 0:
                    A[i][j] = 1
                else:
                    A[i][j] = 0
        
        for i in range(len(A)):
            for j in range(round(len(A[i])/2)):
                A[i][j], A[i][len(A[i]) - 1 - j] = A[i][len(A[i])- 1 - j], A[i][j]
        
        return A



#clever solution

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [[1 ^ i for i in reversed(row)] for row in A]