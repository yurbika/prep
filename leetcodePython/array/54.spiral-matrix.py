class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return
        totalLength = len(matrix)*len(matrix[0])
        arr = []
        i = 0
        j = 0
        while len(arr) < totalLength:
            while j < len(matrix[i]) and matrix[i][j] not in arr:
                arr.append(matrix[i][j])
                j += 1

            i += 1
            j -= 1

            while i < len(matrix) and matrix[i][j] not in arr:
                arr.append(matrix[i][j])
                i += 1

            j -= 1
            i -= 1

            while j > -1 and matrix[i][j] not in arr:
                arr.append(matrix[i][j])
                j -= 1

            i -= 1
            j += 1

            while i > -1 and matrix[i][j] not in arr:
                arr.append(matrix[i][j])
                i -= 1

            j += 1
            i += 1
        return arr
