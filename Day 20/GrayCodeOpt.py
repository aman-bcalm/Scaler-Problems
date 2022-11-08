import sys
import math

sys.setrecursionlimit(10**6)

class Solution:

    def genAns(self, A):

         if A == 0:
            return [0]
         else:
            return self.genAns(A-1) + [A]



    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        return self.genAns(pow(2,A)-1)


obj = Solution()
A = 4
print(obj.grayCode(A))
  