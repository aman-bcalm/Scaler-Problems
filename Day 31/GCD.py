import sys
sys.setrecursionlimit(10**6)

class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
	def gcd(self, A, B):

         if A == 0 or B == 0:
             return A+B
         else:
             return self.gcd(min(A,B), max(A,B) - min(A,B))



obj = Solution()
A = 4
B = 6
print(obj.gcd(A, B))

