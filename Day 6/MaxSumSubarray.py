class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
         
        res = A[0]
        for i in range (0,len(A)):
            i_sum = 0
            for j in range(i,len(A)):
                i_sum = i_sum + A[j]
              
                if i_sum > res :
                    res = i_sum
        return res
        
            
obj = Solution()
A = [1, 2, 3, 4, -10] 
print(obj.maxSubArray(A))