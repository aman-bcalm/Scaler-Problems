class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return a list of integers
	def dNums(self, A, B):
         
         res = []
         fmap = {}
         for i in range(0, B):
             if A[i] in fmap:
                 fmap[A[i]] += 1
             else:
                 fmap[A[i]] = 1

         res.append(len(fmap.keys()))

         for i in range(0,len(A)-B):
            
            #shift window by 1

            #delete A[i] from map
             if A[i] in fmap:
                 if fmap[A[i]] >= 2:
                     fmap[A[i]] -= 1
                 elif fmap[A[i]] == 1:
                     fmap.pop(A[i])
            
            #add i + k into the map
             if A[i+B] in fmap:
                 fmap[A[i+B]] += 1
             else:
                 fmap[A[i+B]] = 1

             #count number of distint keys and put in res
             res.append(len(fmap.keys()))
         
         return res


obj = Solution()
A = [1, 1, 2, 2]
B = 1
obj.dNums(A, B)

                

