class Solution:
	# @param A : list of integers
	# @return a list of integers
	def lszero(self, A):

         
         
         B = A.copy()
         S1 = 0
         mp = {}
         max  = 0
         res = []
         for i in range(0, len(A)):
             S1 = S1 + A[i]
             A[i] = S1

             if A[i] == 0:
                 if i+1 > max:
                     max = i+1
                     res = B[0:i+1]
             elif A[i] in mp:
                if i - mp[A[i]] > max:
                    max = i - mp[A[i]]
                    start = mp[A[i]] + 1
                    res = B[start: i+1]
             else:
                mp[A[i]] = i

         return res

    




obj = Solution()
A = [2,-2,4,-4]
print(obj.lszero(A))

        
            

