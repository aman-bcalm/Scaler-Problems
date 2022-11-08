class Solution:
    # @param A : list of integers
     # @return an long
     #time complexity O(N^2)
    def subarraySum(self, A):

        sum = 0
        for i in range(0,len(A)):
            sum = sum + (A[i] * (i+1) * (len(A)-i))
        
        return sum


obj = Solution()
A = [1, 2, 3]
print(obj.subarraySum(A))
                