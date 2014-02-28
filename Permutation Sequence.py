class Solution:
    # @return a string
    def getPermutation(self, n, k):
        k -= 1
        dset = [str(i+1) for i in range(n)]
        seln = 0
        fn = [1]
        for i in range(1, n):
            fn.append(i*fn[i-1])
        while seln < n:
            num = fn[n-seln-1]
            sel = k/num
            tmp = dset[seln]
            dset[seln] = dset[seln+sel]
            for i in range(seln+sel, seln, -1):
                dset[i] = dset[i-1]
            if sel > 0:
                dset[seln+1] = tmp
            k -= sel*num
            seln += 1
        return "".join(dset)