class Solution:
    # @param A : integer
    # @return an integer
    def findAthFibonacci(self, A):

        if A == 0:
            return 0
        elif A == 1:
            return 1
        else:
            return self.findAthFibonacci(A-1) + self.findAthFibonacci(A-2)


obj = Solution()
A = 9
print(obj.findAthFibonacci(A))
