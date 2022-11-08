import sys
sys.setrecursionlimit(10**6)

# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None



class Solution:


    def maxAnces(self, A, mx):


        if A == None:
            return 0
        elif A.val > mx:
            mx = A.val
            return 1 + self.maxAnces(A.left,mx) + self.maxAnces(A.right, mx)
        else:
            return self.maxAnces(A.left,mx) + self.maxAnces(A.right, mx)



    # @param A : root node of tree
    # @return an integer
    def solve(self, A):

        return self.maxAnces(A, -10**9)



obj = Solution()
t1 = TreeNode(4)
t2 = TreeNode(5)
t3 = TreeNode(2)
t4 = TreeNode(3)
t5 = TreeNode(6)
t1.left = t2
t1.right = t3
t3.left = t4
t3.right = t5
print(obj.solve(t1))

       