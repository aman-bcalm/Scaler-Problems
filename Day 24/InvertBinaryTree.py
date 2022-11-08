# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:

	# @param A : root node of tree
	# @return the root node in the tree
	def invertTree(self, A):

         if A == None:
            return None
         else:
             c = self.invertTree(A.left)
             d = self.invertTree(A.right)
             A.left = d
             A.right = c
             return A

obj = Solution()
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t1.left = t2
t1.right = t3
print(t1.left.val)
print(t1.right.val)
obj.invertTree(t1)
print(t1.left.val)
print(t1.right.val)