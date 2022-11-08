class Solution:
    # @param A : list of integers
     # @return an long
     #time complexity O(N^2)
    def subarraySum(self, A):

        sum = 0
        for i in range(0,len(A)):
            sum = sum + A[i]
            A[i] = sum
        print(A)
        sum = 0
        for i in range(0,len(A)):
            for j in range(i,len(A)):
                if i == 0:
                    sum += A[j]
                else:
                    sum += A[j] - A[i-1]
                print(i,j,sum)
        return sum


obj = Solution()
A = [1, 2, 3]
print(obj.subarraySum(A))
                

