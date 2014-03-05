class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        snum = [(num[i], i+1) for i in range(len(num))]
        snum.sort()
        l = 1
        r = len(snum)-1
        while l < r:
            mid = (l+r)//2
            if snum[mid][0] < target-snum[0][0]:
                l = mid+1
            else:
                r = mid
        p1 = 0
        p2 = r
        while p1 < p2:
            while snum[p1][0] + snum[p2][0] > target:
                p2 -= 1
            if snum[p1][0] + snum[p2][0] == target:
                break
            p1 += 1
        if snum[p1][1] > snum[p2][1]:
            return (snum[p2][1],snum[p1][1])
        return (snum[p1][1],snum[p2][1])