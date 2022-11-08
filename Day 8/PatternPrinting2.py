import numpy as np

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        res = []
        for i in range(1,A+1):
            res1 = list(np.arange(1,i+1)) + ([0] * (A-i))
            res1.reverse()
            res.append(res1)
        
        return res

obj = Solution()
A = 3
print(obj.solve(A))        
