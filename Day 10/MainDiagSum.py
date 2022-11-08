class Solution:
    # @param A : tuple of list of integers
    # @return an integer
    def solve(self, A):
        sum = 0
        for i in range(0,len(A)):
            sum += A[i][i]
        return sum

