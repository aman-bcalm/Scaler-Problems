class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):

        res = []
        for i in range(0,len(A)):
            sum = 0
            for j in range(0,len(A[0])):
                sum += A[i][j]
            res.append(sum)
        return res
