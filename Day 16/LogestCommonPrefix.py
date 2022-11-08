class Solution:
	# @param A : list of strings
	# @return a strings
	def longestCommonPrefix(self, A):

         res = []
         #length of smallest string
         sml = len(A[0])
         for i in range(0, len(A)):
             sml = min(sml, len(A[i]))
         
         
         for j in range(0, sml):
            c = A[0][j]
            flag = 1
            for i in range(1, len(A)):
                 if A[i][j] != c:
                     flag = 0
            
            if flag == 1:
                res.append(c)

         res = ''.join(res)
         return res

obj = Solution()
A = ["abab", "ab", "abcd"]
print(obj.longestCommonPrefix(A))
            



