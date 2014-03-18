class Solution:
    def twoSum(self, snum, sp, target):
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
        reslist = []
        while p1 < p2:
            while p1 < p2 and snum[p1] + snum[p2] > target:
                p2 -= 1
            if p1 == p2:
                break
            if snum[p1]+snum[p2] == target:
                reslist.append((snum[p1], snum[p2]))
                while p1 < p2 and snum[p1] + snum[p2] == target:
                    p2 -= 1
            p1 += 1
        return reslist
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num.sort()
        reslist = []
        i = 0
        while i < len(num)-2:
            reslist.extend([[num[i],x[0],x[1]] for x in self.twoSum(num, i+1, -num[i])])
            i += 1
            while i < len(num)-2 and num[i] == num[i-1]:
                i += 1
        return reslist