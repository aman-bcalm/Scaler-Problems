import sys
sys.setrecursionlimit(10**6)

# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : root node of tree
	# @param B : root node of tree
	# @return an integer
	def isSameTree(self, A, B):

         if A == None and B == None:
             return 1
         elif A == None and B != None:
             return 0
         elif B == None and A != None:
             return 0
         elif A.val != B.val:
            return 0
         else:
             c = self.isSameTree(A.left,B.left)
             d = self.isSameTree(A.right,B.right)
             if c == 1 and d == 1:
                 return 1
             else:
                 return 0


obj = Solution()
t1 = TreeNode(1)
t2 = TreeNode(2)
t1.right = t2
t3 = TreeNode(3)
t2.left = t3
print(obj.isSameTree(t1, t1))