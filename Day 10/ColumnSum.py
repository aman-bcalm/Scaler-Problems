class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        res = []
        for j in range(0, len(A[0])):
            sum = 0
            for i in range(0, len(A)):
                sum += A[i][j]
            res.append(sum)
        return res

