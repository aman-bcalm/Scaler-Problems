class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        A.sort()
        res = 1
        diff = A[1] - A[0]
        for i in range(1, len(A)):
            
            if A[i] - A[i-1] != diff :
                res = 0
                break
        
        return res

obj = Solution()
A = [2,4,1]
print(obj.solve(A))
