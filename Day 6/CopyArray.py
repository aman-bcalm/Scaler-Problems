

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        res =[]
        for i in range(0,len(A)):
             res.append(A[i] + B)
        return res