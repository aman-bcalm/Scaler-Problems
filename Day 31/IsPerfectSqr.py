import math

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

       for i in range(1, 10001):

           if i*i == A:
               return 1
       
       return 0


obj = Solution()
A = 4
print(obj.solve(A))
