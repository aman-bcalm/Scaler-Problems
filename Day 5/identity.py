class Solution:
    # @param A : tuple of list of integers
    # @return an integer
    def solve(self, A):
        ans = 1
        for i in range(0, len(A)):
            if A[i][i] != 1:
                ans =0
                break
        return ans
