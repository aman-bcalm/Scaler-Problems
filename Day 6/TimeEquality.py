class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        max = A[0]
        size = len(A)

        for i in range (0,size) :
            if A[i] > max:
                max = A[i]
        
        total_sec = 0
        for i in range (0,size):
            total_sec = total_sec + (max - A[i])
        
        return total_sec
    

obj = Solution()
A = [2,4,1,3,2]
print(obj.solve(A))

