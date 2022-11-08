class Solution:


    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def pow(self, A, B, C):

        if A == 0:
            return 0

        if B == 0:
            return 1
        else:
            return ((A%C) * pow(A, B-1, C))%C


A = 0
B = 0
C = 1
obj = Solution()
print(obj.pow(A,B,C))