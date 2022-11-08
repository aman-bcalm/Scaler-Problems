import sys

class Solution:
	# @param A : list of integers
	# @return a list of integers
	def lszero(self, A):

        
         st = {}
         sumt = 0
         res = 0 
         for i in range(0, len(A)):
            sumt += A[i]
            st[i] = sumt
        
         print(st) 
         shmap = {}
         for key in st:

            if st[key] in shmap:
             shmap[st[key]].append(key)
            else:
              shmap[st[key]] = [key]    
         
         print(shmap)
         il = []
         l_l = -sys.maxsize-1
         for key in shmap:
            if len(shmap[key]) > l_l:
               l_l = len(shmap[key])
               il = shmap[key]
         
         




         #i_l =[]
         #mlk = 0
         #res_k = 0
         #for key in shmap:

          #   if len(shmap[key]) > mlk:
           #      mlk = len(shmap[key])
           #      res_k = key
         #print(res_k,mlk, shmap[res_k])
         #print(shmap[res_k][0], shmap[res_k][len(shmap[res_k])-1])
         ##
         




obj = Solution()
A = [2,-2,4,-4,5,3,-2,-6]
print(obj.lszero(A))