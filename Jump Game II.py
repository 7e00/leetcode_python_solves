class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        steps = [-1]*len(A)
        q = [0]*(len(A)+1)
        head = 0
        tail = 1
        steps[0] = 0
        while head != tail:
            p = q[head]
            head += 1
            if p+A[p] >= len(A)-1:
                return steps[p]+1 if p < len(A)-1 else steps[p]
            for i in range(A[p],0,-1):
                if steps[p+i] != -1:
                    break
                steps[p+i] = steps[p]+1
                q[tail] = p+i
                tail += 1
        return steps[len(A)-1]