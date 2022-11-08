import sys

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        ls = 0
        res = 0
        for i in range(0,B):
            ls = ls + A[i]
        
        min_g = ls

        for i in range(1,len(A)-B+1):
            
            cs = ls - A[i-1] + A[i+B-1]

            if min_g > cs :
                min_g = cs
                res = i
            
            ls = cs
            
        return res


obj = Solution()
A=[3, 7, 5, 20, -10, 0, 12]
B=2
print(obj.solve(A,B))

