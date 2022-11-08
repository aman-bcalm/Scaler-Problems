import math

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):

        fc = 1
        fc_n = A[0]

        for i in range(1, len(A)):

            if A[i] == fc_n:
                fc += 1
            else:
                if fc == 0:
                    fc = 1
                    fc_n = A[i]
                else:
                    fc -= 1
                    if fc == 0:
                        fc_n = None
                
                

        
        if fc > 0:
            c = 0
            for i in range(0,len(A)):
                if A[i] == fc_n:
                    c += 1
            
            if c > math.floor(len(A)/2):
                return fc_n
        else:
            return -1


obj = Solution()
A = [2,1,2]
print(obj.majorityElement(A))



