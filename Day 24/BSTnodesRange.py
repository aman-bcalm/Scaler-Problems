# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):

        if A == None:
            return 0

        N = A.val

        if N < B :
            return self.solve(A.right, B, C)
        
        elif C < N :
            return self.solve(A.left, B, C)


        elif N >= B and N <=C :
            return 1 + self.solve(A.left, B , C) + self.solve(A.right, B , C)

       

    


obj = Solution()
t1 = TreeNode(8)
t2 = TreeNode(6)
t3 = TreeNode(21)
t4 = TreeNode(1)
t5 = TreeNode(4)
t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5
print(obj.solve(t1, 2, 20))

