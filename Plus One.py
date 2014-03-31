class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        res = [0]*(len(digits)+1)
        res[0] = 1
        for i in range(len(digits)):
            res[i] += digits[len(digits)-i-1]
            res[i+1] += (res[i]//10)
            res[i] %= 10
        i = len(res)-1
        while i > 0 and res[i] == 0:
            i -= 1
        return res[i::-1]