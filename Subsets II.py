class Solution:
    def getsubset(self, S, sp, subset, elemn):
        if sp == len(S):
            self.subsetlist.append(subset[:elemn])
            return
        for i in range(sp, len(S)):
            if S[i] != S[sp]:
                break
        else:
            i = len(S)
        num = i - sp
        self.getsubset(S, sp+num, subset, elemn)
        for i in range(1,num+1):
            subset[elemn+i-1] = S[sp]
            self.getsubset(S, sp+num, subset, elemn+i)
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        self.subsetlist = []
        subset = S[:]
        self.getsubset(sorted(S), 0, subset, 0)
        return self.subsetlist