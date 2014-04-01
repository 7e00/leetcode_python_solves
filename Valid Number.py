class Solution:
    dfa = [{} for i in range(9)]
    dfa[0] = {'+':4, '-':4, '.':6, 0:1}
    dfa[1] = {0:1, '.':2, 'e':7, 'E':7}
    dfa[2] = {0:2, 'e':7, 'E':7}
    dfa[3] = {0:3}
    dfa[4] = {'.':5, 0:1}
    dfa[5] = {0:2}
    dfa[6] = {0:2}
    dfa[7] = {'+':8, '-':8, 0:3}
    dfa[8] = {0:3}
    def go(self, statu, x):
        if x in self.dfa[statu]:
            return self.dfa[statu][x]
        return None
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        statu = 0
        for x in s.strip():
            if ord(x) >= ord('0') and ord(x) <= ord('9'):
                statu = self.go(statu, 0)
            else:
                statu = self.go(statu, x)
            if statu == None:
                break
        return True if statu and statu <= 3 else False