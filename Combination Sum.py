class Solution:
    def solve(self, candidates, n, target):
        if n == len(candidates):
            if target == 0:
                ans = []
                for i in range(len(candidates)-1,-1,-1):
                    for j in range(self.cnts[i]):
                        ans.append(candidates[i])
                self.listres.append(ans)
            return
        if n > 0 and candidates[n] == candidates[n-1]:
            self.slove(candidates, n+1, target)
        else:
            if n == len(candidates)-1:
                if target%candidates[n] != 0:
                    return
                else:
                    cnt = self.cnts[n]
                    self.cnts[n] = target//candidates[n]
                    self.solve(candidates, n+1, 0)
                    self.cnts[n] = cnt
                    return
            self.solve(candidates, n+1, target)
            cnt = self.cnts[n]
            while target >= candidates[n]:
                target -= candidates[n]
                self.cnts[n] += 1
                self.solve(candidates, n+1, target)
            self.cnts[n] = cnt
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates.sort(reverse = True)
        self.cnts = [0]*len(candidates)
        self.listres = []
        self.solve(candidates, 0, target)
        return self.listres