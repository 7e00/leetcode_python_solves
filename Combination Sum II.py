class Solution:
    def solve(self, candidates, n, target):
        if n == self.clen:
            if target == 0:
                ans = []
                for i in range(self.clen-1,-1,-1):
                    for j in range(self.seln[i]):
                        ans.append(candidates[i])
                self.reslist.append(ans)
            return
        if self.sums[n] < target:
            return
        if target == 0:
            self.solve(candidates, self.clen, 0)
            return
        if target < candidates[self.clen-1]:
            return
        self.solve(candidates, n+1, target)
        cnt = 0
        while target >= candidates[n] and cnt < self.nums[n]:
            target -= candidates[n]
            cnt += 1
            self.seln[n] = cnt
            self.solve(candidates, n+1, target)
        self.seln[n] = 0
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        candidates.sort(reverse = True)
        self.clen = 0
        self.nums = []
        for i in range(len(candidates)):
            if i == 0 or candidates[i] != candidates[i-1]:
                self.nums.append(1)
                candidates[self.clen] = candidates[i]
                self.clen += 1
            else:
                self.nums[self.clen-1] += 1
        self.sums = [0]*self.clen
        self.sums[self.clen-1] = candidates[self.clen-1]*self.nums[self.clen-1]
        for i in range(self.clen-2,-1,-1):
            self.sums[i] = self.sums[i+1] + candidates[i]*self.nums[i]
        self.seln = [0]*self.clen
        self.reslist = []
        self.solve(candidates, 0, target)
        return self.reslist