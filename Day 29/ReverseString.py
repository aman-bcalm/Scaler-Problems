class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):

        A = A.split()
        A.reverse()
        A = " ".join(A)
        return A

obj = Solution()
A = "this is ib"  
print(obj.solve(A))
