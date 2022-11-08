class Solution:
    # @param A : tuple of list of integers
    # @return an integer
    def solve(self, A):
        sum = 0
        for i in range(0,len(A)):
            for j in range(0,len(A[0])):

                if i+1+j+1 == len(A) + 1:
                    sum += A[i][j]
        return sum

