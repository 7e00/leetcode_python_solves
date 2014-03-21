class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        for row in range(9):
            m = [False]*10
            for i in range(9):
                if board[row][i] == '.':
                    continue
                if int(board[row][i]) < 1 or int(board[row][i]) > 9:
                    return False
                if m[int(board[row][i])]:
                    return False
                m[int(board[row][i])] = True
        for col in range(9):
            m = [False]*10
            for i in range(9):
                if board[i][col] == '.':
                    continue
                if int(board[i][col]) < 1 or int(board[i][col]) > 9:
                    return False
                if m[int(board[i][col])]:
                    return False
                m[int(board[i][col])] = True
        for i in range(0,9,3):
            for j in range(0,9,3):
                m = [False]*10
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        if board[k][l] == '.':
                            continue
                        if int(board[k][l]) < 1 or int(board[k][l]) > 9:
                            return False
                        if m[int(board[k][l])]:
                            return False
                        m[int(board[k][l])] = True
        return True