class Solution:
    def bfs(self, board, vis, pset, r, c):
        vis[r][c] = True
        maxsize = len(board)*len(board[0])+1
        q = [(r,c)]
        head = 0
        res = True
        while head != len(q):
            r,c = q[head]
            head += 1
            pset.append((r,c))
            if r == 0 or r == len(board)-1 or c == 0 or c == len(board[0])-1:
                res = False
            if r > 0 and board[r-1][c] == "O" and not vis[r-1][c]:
                vis[r-1][c] = True
                q.append((r-1,c))
            if r < len(board)-1 and board[r+1][c] == "O" and not vis[r+1][c]:
                vis[r+1][c] = True
                q.append((r+1,c))
            if c > 0 and board[r][c-1] == "O" and not vis[r][c-1]:
                vis[r][c-1] = True
                q.append((r,c-1))
            if c < len(board[0])-1 and board[r][c+1] == "O" and not vis[r][c+1]:
                vis[r][c+1] = True
                q.append((r,c+1))
        return res
    # @param board, a 9x9 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        sta = [[False for i in range(len(board[0]))] for j in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and not sta[i][j]:
                    pset = []
                    res = self.bfs(board, sta, pset, i, j)
                    if res:
                        for r,c in pset:
                            board[r][c] = "X"