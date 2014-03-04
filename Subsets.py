class Solution:
    def getsubsets(self, S, n, subset, elemn):
        if n == len(S):
            self.subsetlist.append(subset[:elemn])
            return
        self.getsubsets(S, n+1, subset, elemn)
        subset[elemn] = S[n]
        self.getsubsets(S, n+1, subset, elemn+1)
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        self.subsetlist = []
        subset = S[:]
        self.getsubsets(sorted(S), 0, subset, 0)
        return self.subsetlist