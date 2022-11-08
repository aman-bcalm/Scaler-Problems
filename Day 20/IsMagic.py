class Solution:

    def Sum(self, A):

        if A/10 < 1:
            return A
        else:
            return A%10 + self.Sum(int(A/10))

    # @param A : integer
    # @return an integer
    def solve(self, A):

        if self.Sum(A) / 10  == 1:    
            return 1

        elif  self.Sum(A) / 10 > 1:
            return self.solve(self.Sum(A))

        else:
            return 0

obj = Solution()
A = 17
print(obj.solve(A))

