class Solution:
	# @param A : tuple of integers
	# @return an integer
	def longestConsecutive(self, A):

         s = set()
         for i in range(0, len(A)):
             s.add(A[i])
         
         f_res = 0
         for i in range(0, len(A)):

             if not(A[i]-1 in s):
                 res = 0
                 x = A[i]
                 while x in s:
                     res += 1
                     x += 1
                 f_res = max(f_res, res)
         
         return f_res

obj = Solution()
A  = [2, 1]
print(obj.longestConsecutive(A))

