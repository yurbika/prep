class Solution:
    def dfs(self, board, i, j, pos, word):
        if pos == len(word):
            return True

        if i < 0 or i >= len(board) or j >= len(board[i]) or j < 0 or board[i][j] != word[pos]:
            return False

        temp = board[i][j]
        board[i][j] = ' '

        found = self.dfs(board, i+1, j, pos+1, word)
        if not found:
            found = self.dfs(board, i-1, j, pos+1, word)
        if not found:
            found = self.dfs(board, i, j+1, pos+1, word)
        if not found:
            found = self.dfs(board, i, j-1, pos+1, word)

        board[i][j] = temp
        return found

    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0] and self.dfs(board, i, j, 0, word):
                    return True

        return False
