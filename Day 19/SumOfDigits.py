class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        if A/10 < 1:
            return A
        else:
            return (A % 10) + self.solve(int(A/10))

obj = Solution()
A = 11
print(obj.solve(A))
