class Solution:
    def right(self, matrix, layer, r, c, res):
        for j in range(c+1,len(matrix[0])-layer):
            res.append(matrix[r][j])
        else:
            return r, j
    def down(self, matrix, layer, r, c, res):
        for i in range(r+1, len(matrix)-layer):
            res.append(matrix[i][c])
        else:
            return i, c
    def left(self, matrix, layer, r, c, res):
        for j in range(c-1, layer-1, -1):
            res.append(matrix[r][j])
        else:
            return r, j
    def up(self, matrix, layer, r, c, res):
        for i in range(r-1, layer, -1):
            res.append(matrix[i][c])
        else:
            return i, c
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if len(matrix) == 0:
            return []
        tnum = len(matrix)*len(matrix[0])
        r, c = 0, -1
        res = []
        for layer in range((min(len(matrix),len(matrix[0]))+1)//2):
            r, c = self.right(matrix, layer, r, c, res)
            if len(res) == tnum:
                break
            r, c = self.down(matrix, layer, r, c, res)
            if len(res) == tnum:
                break
            r, c = self.left(matrix, layer, r, c, res)
            if len(res) == tnum:
                break
            r, c = self.up(matrix, layer, r, c, res)
            if len(res) == tnum:
                break
        return res