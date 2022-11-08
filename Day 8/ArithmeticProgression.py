class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        res = 1
        A.sort()
        step = A[1] - A[0]
        for i in range(1,len(A)):
            if A[i] - A[i-1] != step:
                res = 0
                break
        return res

obj = Solution()
A = [3, 5, 1]
print(obj.solve(A))

        
