import math

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def LCM(self, A, B):

        prod = A*B
        C = max(A,B)
        res = C
        for i in range(C,prod+1):
            if i%A == 0 and i%B == 0:
                res =i
                break
        return res








obj = Solution()
print(obj.LCM(4,6))