class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return a list of list of integers
    def solve(self, A, B):

        for i in range(0,len(A)):
            for j in range(0,len(A[0])):
                A[i][j] = B * A[i][j]
        return A
