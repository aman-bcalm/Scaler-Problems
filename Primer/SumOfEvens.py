class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        S = 0
        for i in range(1,A+1):

            if i % 2 == 0:
                S += i
        return S

obj = Solution()
A = 2
print(obj.solve(A))
