# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:

    #fill up l with the path if exists
    def find(self, A, B, l):

        if A == None:
            return False

        l.append(A.val)        
        if A.val == B:
            return True

        if self.find(A.left, B, l) or self.find(A.right, B, l):
            return True
        
        l.pop(-1)
        return False

             

    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        
        ans = []
        self.find(A,B, ans)
        return ans   




obj = Solution()
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t6 = TreeNode(6)
t7 = TreeNode(7)
t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5
t3.left = t6
t3.right = t7
print(obj.solve(t1,4))




