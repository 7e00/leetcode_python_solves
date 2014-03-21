class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        sta = []
        top = 0
        res = 0
        intval = []
        itop = 0
        preintval = [0,-1]
        for i in range(len(s)):
            if s[i] == '(':
                if top == len(sta):
                    sta.append(i)
                else:
                    sta[top] = i
                top += 1
            else:
                if top != 0:
                    while itop and intval[itop-1][0] > sta[top-1]:
                        itop -= 1
                    if itop and intval[itop-1][1]+1 == sta[top-1]:
                        intval[itop-1][1] = i
                    else:
                        if itop == len(intval):
                            intval.append([sta[top-1], i])
                        else:
                            intval[itop] = [sta[top-1], i]
                        itop += 1
                    res = max(res, intval[itop-1][1]-intval[itop-1][0]+1)
                    top -= 1
        return res