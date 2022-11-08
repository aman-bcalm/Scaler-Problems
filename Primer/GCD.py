import math

class Solution:

     def isPrime(self, A):
        c = 0
        ub = int(math.sqrt(A))
        for i in range(1,ub+1):
            if A % i  == 0:
                c += 1
            if c >= 2:
                break
        if c >=2:
            return 1
        else :
            return 0
            

                

            
        


	# @param A : integer
	# @param B : integer
	# @return an integer
     def gcd(self, A, B):

         if A == 0 or B == 0:
            return max(A,B)

         if self.isPrime(A) or self.isPrime(B):
             return 1
            
         sml = min(A, B)
         res = -1
         for i in range(sml,0,-1):
             if A % i == 0 and B % i == 0 :
                 res = i
                 break
         return res

obj = Solution()
A = 2
B = 2
print(obj.gcd(A,B))

                 
            
           
        





