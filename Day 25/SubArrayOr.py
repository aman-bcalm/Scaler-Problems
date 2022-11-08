import math

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        TS = 0

        for i in range(0, len(A)):

            p = 0
            for j in range(i, len(A)):
                p = p | A[j]
                TS += p
            
            
        bn = math.pow(10,9) + 7
        res = int(TS%bn)
        return res

obj = Solution()
A = [7,8,9,10]
print(obj.solve(A))


