class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):

        res = 1
        for i in range(0,len(A)):
            for j in range(0,len(A[0])):
                if A[i][j] != B[i][j]:
                    res = 0
                    break
            if res == 0:
                break
        return res
