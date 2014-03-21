class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        for i in range(len(num)-1,0,-1):
            if num[i] > num[i-1]:
                tmp = num[i-1]
                j = i
                k = len(num)-1
                while j < k:
                    tt = num[j]
                    num[j] = num[k]
                    num[k] = tt
                    j += 1
                    k -= 1
                l = i
                r = len(num)-1
                while l < r:
                    mid = (l+r)//2
                    if num[mid] <= tmp:
                        l = mid+1
                    else:
                        r = mid
                num[i-1] = num[r]
                num[r] = tmp
                break
        else:
            num.reverse()
        return num