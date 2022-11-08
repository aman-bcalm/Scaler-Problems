import math

class Solution:


    # @param A : list of integers
	# @return an integer
    def solve(self, A):

        A.sort()
        Sum = 0

        for i in range(0, len(A)):

            maxi = A[i] * pow(2,i)
            mini = A[i] * pow(2, len(A) - 1 - i)

            Sum += (maxi - mini)
        Sum = Sum % 1000000007
        return Sum


obj = Solution()
A = [1]
print(obj.solve(A))



