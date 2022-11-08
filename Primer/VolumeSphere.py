import math 
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        res = (float(4*math.pi*A*A*A)/3)
        res = math.ceil(res)
        return res
       

obj = Solution()
obj.solve(4)
