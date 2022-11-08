class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def solve(self, A):
        ans = []
        for i in range(len(A)-1,-1,-1):
            ans.append(A[i])
        return ans
