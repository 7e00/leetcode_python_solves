class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1:
            return s
        rowwords = [[] for i in range(nRows)]
        row = 0
        step = 1
        for letter in s:
            rowwords[row].append(letter)
            row += step
            if row < 0 or row >= nRows:
                row -= step
                step = -step
                row += step
        return "".join(["".join(rowwords[i]) for i in range(nRows)])