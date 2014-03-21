class Solution:
    def check(self, row, col, val):
        if self.Rows[row] & (1<<(val-1)):
            return False
        if self.Cols[col] & (1<<(val-1)):
            return False
        if self.Grids[(row//3)*3 + (col//3)] & (1<<(val-1)):
            return False
        return True
    def solve(self, diboard, r):
        for i in range(r, 9):
            for j in range(0, 9):
                if diboard[i][j] == 0:
                    for k in range(1,10):
                        if self.check(i, j, k):
                            self.Rows[i] |= (1<<(k-1))
                            self.Cols[j] |= (1<<(k-1))
                            self.Grids[(i//3)*3+(j//3)] |= (1<<(k-1))
                            diboard[i][j] = k
                            if self.solve(diboard, i):
                                return True
                            self.Rows[i] ^= (1<<(k-1))
                            self.Cols[j] ^= (1<<(k-1))
                            self.Grids[(i//3)*3+(j//3)] ^= (1<<(k-1))
                    else:
                        diboard[i][j] = 0
                        return False
        return True
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        diboard = [[(lambda x: 0 if x == '.' else int(x))(letter) for letter in s] for s in board]
        self.Rows = [0]*9
        self.Cols = [0]*9
        self.Grids = [0]*9
        for i in range(9):
            for j in range(9):
                if diboard[i][j] == 0:
                    continue
                self.Rows[i] |= (1<<(diboard[i][j]-1))
                self.Cols[j] |= (1<<(diboard[i][j]-1))
                self.Grids[(i//3)*3+(j//3)] |= (1<<(diboard[i][j]-1))
        self.solve(diboard, 0)
        for i in range(9):
            board[i] = "".join([str(x) for x in diboard[i]])