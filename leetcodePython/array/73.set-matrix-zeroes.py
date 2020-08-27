class Solution:
    def row(self, matrix, i):
        for j in range(len(matrix[0])):
            matrix[i][j] = 0

    def col(self, matrix, j):
        for i in range(len(matrix)):
            matrix[i][j] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = []
        col = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    col.append(j)
                    row.append(i)

        for i in range(len(row)):
            self.col(matrix, col[i])
        for i in range(len(col)):
            self.row(matrix, row[i])
