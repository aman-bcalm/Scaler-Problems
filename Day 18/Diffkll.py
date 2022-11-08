class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
	def diffPossible(self, A, B):
         
         if len(A) <= 1:
             return 0
         s = set()
         res = 0
         for i in range(0, len(A)):

             if A[i] - B in s :
                 #print(i,A[i],A[i]-B)
                 res = 1
                 break
             if B + A[i] in s :
                 #print(i,A[i],B - A[i])
                 res = 1
                 break
             s.add(A[i])
         return res

obj = Solution()
A = [ 34, 63, 64, 38, 65, 83, 50, 44, 18, 34, 71, 80, 22, 28, 20, 96, 33, 70, 0, 25, 64, 96, 18, 2, 53, 100, 24, 47, 98, 69, 60, 55, 8, 38, 72, 94, 18, 68, 0, 53, 18, 30, 86, 55, 13, 93, 15, 43, 73, 68, 29 ]
B = 97
print(obj.diffPossible(A,B))

              

