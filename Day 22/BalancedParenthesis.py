class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):

        c = 0
        for i in range(0, len(A)):
            if A[i] == '(':
                c += 1
            elif A[i] == ')':
                c -= 1
        
        if c == 0:
            return 1
        else:
            return 0

obj = Solution()
A = "(()"
print(obj.solve(A))
