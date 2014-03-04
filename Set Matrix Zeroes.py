class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        col = row = False
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    if i == 0:
                        row = True
                    if j == 0:
                        col = True
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(len(matrix[i])):
                    matrix[i][j] = 0
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(len(matrix)):
                    matrix[i][j] = 0
        if col:
            for i in range(0, len(matrix)):
                matrix[i][0] = 0
        if row:
            for j in range(0, len(matrix[0])):
                matrix[0][j] = 0