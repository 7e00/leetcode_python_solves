class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        if target < matrix[0][0] or target > matrix[m-1][n-1]:
            return False
        l = 0
        r = m-1
        while l < r:
            mid = (l+r)//2
            if matrix[mid][n-1] < target:
                l = mid + 1
            elif matrix[mid][n-1] > target:
                r = mid
            else:
                return True
        row = l
        l = 0
        r = n-1
        while l <= r:
            mid = (l+r)//2
            if matrix[row][mid] < target:
                l = mid+1
            elif matrix[row][mid] > target:
                r = mid-1
            else:
                return True
        return False