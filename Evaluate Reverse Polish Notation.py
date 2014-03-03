# there are some difference between C/C++ and Python about the "divide" operation
# e.g. C/C++: 6/-7 = 0    Python: 6/-7 = -1
# be careful!

class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        numlist = []
        top = 0
        for word in tokens:
            if word[0] == '+':
                c = numlist[top-2] + numlist[top-1]
                top -= 2
            elif word[0] == '-' and len(word) == 1:
                c = numlist[top-2] - numlist[top-1]
                top -= 2
            elif word[0] == '*':
                c = numlist[top-2] * numlist[top-1]
                top -= 2
            elif word[0] == '/':
                b = numlist[top-1]
                a = numlist[top-2]
                if a*b < 0:
                    c = -((-a)//b) if a < 0 else -(a//(-b))
                else:
                    c = a // b
                top -= 2
            else:
                c = int(word)
            if top == len(numlist):
                numlist.append(c)
            else:
                numlist[top] = c
            top += 1
        return numlist[0]