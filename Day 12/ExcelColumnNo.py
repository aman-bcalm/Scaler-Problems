import math
class Solution:
	# @param A : string
	# @return an integer
	def titleToNumber(self, A):

         al = {}
         for i in range(65, 91):
            
            al[chr(i)] = (i-64)
         
         j = 0
         S = 0
         for i in range(len(A)-1,-1,-1):
             S += (al[A[i]] * math.pow(26,j))
             j += 1

         S = int(S)
         return S
         
        

obj = Solution()
A = "ABCD"
print(obj.titleToNumber(A))
        


