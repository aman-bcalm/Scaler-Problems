import math

class Solution:
	# @param A : integer
	# @return an integer
	def colorful(self, A):

        #need to find number of digits
         sn = str(A)
         digits = len(sn)
         
         prd = {}
         t_sub = 0
         for i in range(1,len(sn)+1):

             for j in range(0,len(sn)-i+1):
                 sub = sn[j:j+i]
                
                 prod = 1
                 for k in range(0,len(sub)):
                     prod = prod * int(sub[k])

                 if prod in prd :
                     return 0
                 else :
                     prd[prod] = int(sub)
         
         
         
         
         return 1
         
         
         

                     

                 



obj = Solution()
A = 236
print(obj.colorful(A))

