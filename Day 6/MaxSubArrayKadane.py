
#Kadane's algo
#time complexity O(N)
#space complexity O(1)
class Solution:
    # @param A : list of integers
    # @return an integer
    
    def maxSubArray(self, A):
         mcs = A[0]
         for i in range(1,len(A)): 
            A[i] = max(A[i], A[i-1] + A[i])
            
            if mcs < A[i]:
                mcs = A[i]
          
         return mcs
        
        
            
obj = Solution()
A = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
print(obj.maxSubArray(A))