import math

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        pp = 0
        for i in range(0,len(A)):
            if A[i] < 2 :
                continue
            else :
                c = 0
                for j in range(2, (int)(math.sqrt(A[i]))+1):
                    if A[i] % j == 0:
                       c = 1
                       break
                if c == 0:
                    pp = pp + 1
        return pp


obj = Solution()
A  = [-6, 10, 12]
print(obj.solve(A))