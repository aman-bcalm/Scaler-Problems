# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

#left, root, right
class Solution:

    l = None

    def __init__(self):
        self.l = []

	# @param A : root node of tree
	# @return a list of integers
    def inorderTraversal(self, A):

         if A == None:
             return
         self.inorderTraversal(A.left)
         self.l.append(A.val)
         self.inorderTraversal(A.right)
         return self.l

obj = Solution()
t1 = TreeNode(1)
t2 = TreeNode(2)
t1.right = t2
t3 = TreeNode(3)
t2.left = t3
print(obj.inorderTraversal(t1))
