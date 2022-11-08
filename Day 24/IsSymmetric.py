# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None



# Definition for a  binary tree node
class Solution:

    def isSameTree(self, A, B):

         if A == None and B == None:
            return 1
         
         if A == None or B == None:
             return 0
            
         if A.val != B.val:
             return 0

         return self.isSameTree(A.left, B.right) and self.isSameTree(A.right, B.left)



    def isSymmetric(self, A):

        if A == None:
            return 0
        else:
            return self.isSameTree(A.left, A.right) 


	
obj = Solution()
t1 = TreeNode(1)
t2 = TreeNode(3)
t3 = TreeNode(3)
t1.left = t2
t1.right = t3
print(obj.isSymmetric(t1))


