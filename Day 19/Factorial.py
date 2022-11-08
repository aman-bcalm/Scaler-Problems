class Solution:


    # @param A : integer
    # @return an integer
    def solve(self, A):
        
        if A == 0:
            return 1
        else:
            return A * self.solve(A-1)

obj = Solution()
A = 0
print(obj.solve(A))