x = 11  # results in 2680 possibilities
test = 1


def nQueens(n):
    arr = [[0 for j in range(n)] for i in range(n)]
    solveNQueens(0, arr)


def isValid(board, y, x):
    cnt = 0
    for i in range(len(board)):
        if cnt > 0:
            break
        if y - i >= 0:
            cnt += board[y-i][x]
        if x - i >= 0:
            cnt += board[y][x-i]
        if y + i <= len(board)-1:
            cnt += board[y+i][x]
        if x + i <= len(board)-1:
            cnt += board[y][x+i]
        if x + i <= len(board)-1 and y + i <= len(board)-1:
            cnt += board[y+i][x+i]
        if x - i >= 0 and y + i <= len(board)-1:
            cnt += board[y+i][x-i]
        if x - i >= 0 and y - i >= 0:
            cnt += board[y-i][x-i]
        if x + i <= len(board)-1 and y - i >= 0:
            cnt += board[y-i][x+i]

    if cnt > 0:
        return False
    else:
        return True


def solveNQueens(n, board):
    if n == x:
        # for row in board:
        #     print(row)
        # print("\n")
        global test
        print(test)
        test += 1
        return board
    else:
        for i in range(len(board)):
            if i > 0 and sum(board[i-1]) == 0:
                if board[n].count(1) == 1:
                    board[n][board[n].index(1)] = 0
                return board
            for j in range(len(board)):
                if isValid(board, i, j):
                    board[i][j] = 1
                    board = solveNQueens(n+1, board)
                    if board[n].count(1) == 1:
                        board[n][board[n].index(1)] = 0
        if board[n].count(1) == 1:
            board[n][board[n].index(1)] = 0

    return board


nQueens(x)
