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
           return 1 + self.solve(A.left) + self.solve(A.right)
