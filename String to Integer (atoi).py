class Solution:
    # @return an integer
    def atoi(self, str):
        x = 0
        sign = 1
        for i in range(len(str)):
            if not str[i].isspace():
                break
        else:
            return 0
        if str[i] == '+':
            sign = 1
        elif str[i] == '-':
            sign = -1
        elif str[i] >= '0' and str[i] <= '9':
            x = int(str[i])
        else:
            return 0
        for j in range(i+1,len(str)):
            if str[j] >= '0' and str[j] <= '9':
                x = x*10 + int(str[j])
            else:
                break
        x *= sign
        return min(2147483647, max(x,-2147483648))