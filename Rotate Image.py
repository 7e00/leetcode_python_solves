class Solution:
    def get_coo(self, N, layer, idx):
        n = N - 2*layer
        if idx < n:
            return layer,layer+idx
        elif idx < 2*n-1:
            return idx-n+1+layer,N-layer-1
        elif idx < 3*n-2:
            return N-layer-1,3*n-3-idx+layer
        else:
            return 4*n-4-idx+layer,layer
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        N = len(matrix)
        for i in range(N/2):
            n = N-2*i
            num = 4*n-4
            for j in range(n-1):
                cooj = self.get_coo(N, i, j)
                jval = matrix[cooj[0]][cooj[1]]
                nextj = (j+n-1)%num
                for k in range(4):
                    nextjcoo = self.get_coo(N, i, nextj)
                    nextjval = matrix[nextjcoo[0]][nextjcoo[1]]
                    matrix[nextjcoo[0]][nextjcoo[1]] = jval
                    jval = nextjval
                    nextj = (nextj+n-1)%num
        return matrix