class Solution:
	# @param A : string
	# @return an integer
	def solve(self, A):

         self.l = []
         self.p = [')','}',']']
         for i in range(0, len(A)):

             if A[i] == '(' or A[i] == '{' or A[i] == '[':
                 self.l.append(A[i])
             elif A[i] in self.p and len(self.l) == 0:
                 return 0
             elif A[i] == ')' and self.l[-1] == '(':
                 self.l.pop()
             elif A[i] == '}' and self.l[-1] == '{':
                 self.l.pop()
             elif A[i] == ']' and self.l[-1] == '[':
                 self.l.pop()
             else:
                 break
        
         if len(self.l) == 0:
             return 1
         else:
             return 0

            
obj = Solution()
A = "))))))))"
print(obj.solve(A))


