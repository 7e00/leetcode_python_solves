class Solution:
    def twoSumColsest(self, snum, sp, target):
        l = sp+1
        r = len(snum)-1
        while l < r:
            mid = (l+r)//2
            if snum[mid] < target-snum[sp]:
                l = mid+1
            else:
                r = mid
        p1 = sp
        p2 = r
        best = snum[p1]+snum[p2]
        while p1 < p2:
            while p1 < p2 and snum[p1] + snum[p2] > target:
                p2 -= 1
            if p1 == p2:
                if snum[p1]+snum[p1+1]-target < abs(best-target):
                    best = snum[p1]+snum[p1+1]
                break
            if snum[p1]+snum[p2] == target:
                best = target
                break
            if target-snum[p1]-snum[p2] < abs(best-target):
                best = snum[p1]+snum[p2]
            if p2 < r and snum[p1]+snum[p2+1]-target < abs(best-target):
                best = snum[p1]+snum[p2+1]
            p1 += 1
        return best
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        closet = num[0]+num[1]+num[2]
        for i in range(len(num)-2):
            best = self.twoSumColsest(num, i+1, target - num[i])
            if abs(best+num[i]-target) < abs(closet-target):
                closet = best+num[i]
                if closet == target:
                    break
        return closet