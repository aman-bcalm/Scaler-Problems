class Solution:


	# @param A : string
	# @return a strings
 def longestPalindrome(self, A):
         
         res = -1
         res_i, res_j = -1, -1
         for i in range(0, len(A)):

             ol = self.lenPalindrome(i,i,A)
             el = self.lenPalindrome(i, i+1,A)
             oll = ol[1] - ol[0] - 1
             ell = el[1] - el[0] - 1
             if ell > oll and ell > res:
                 res_i = el[0]
                 res_j = el[1]
                 res = el[1] - el[0] -1
             elif oll  > ell and oll > res:
                 res_i = ol[0]
                 res_j = ol[1]
                 res = ol[1] - ol[0] -1
         
         B = []
         for i in range(res_i+1, res_j):
             B.append(A[i])

         C = ''.join(B)
         return C



 def lenPalindrome(self, start, end, A):
        i = start
        j = end

        while (i >= 0 and j < len(A)) and A[i] == A[j] :
            i -= 1
            j += 1
    
        return [i,j]



obj = Solution()
A = "aaaabaaa"
print(obj.longestPalindrome(A))


             




