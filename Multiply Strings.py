class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        res = [0]*(len(num1)+len(num2))
        for i in range(len(num1)):
            d = int(num1[len(num1)-i-1])
            for j in range(len(num2)):
                res[i+j] += d*int(num2[len(num2)-j-1])
                res[i+j+1] += res[i+j]//10
                res[i+j] %= 10
        i = len(res)-1
        while i > 0 and res[i] == 0:
            i -= 1
        return "".join([str(res[j]) for j in range(i, -1, -1)])