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
    # @return an integer
    def solve(self, A):

        if A == None:
            return 0
        else:
             return 1 + max(self.solve(A.left), self.solve(A.right))


obj = Solution()
t1 = TreeNode(1)
t2 = TreeNode(4)
t3 = TreeNode(3)
t4 = TreeNode(2)
t1.left = t2
t1.right = t3
t2.left = t4
print(obj.solve(t1))