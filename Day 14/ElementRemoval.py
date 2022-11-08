class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        A.sort()
        S = A[0]
        for i in range(1, len(A)):

            S = S + A[i]
            A[i] = S

        ts = 0
        for i in range(0, len(A)):
            ts = ts + A[i]
        
        return ts


obj = Solution()
A = [3, 2, 1, 3]
print(obj.solve(A))
        
        
            
