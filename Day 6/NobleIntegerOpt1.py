class Solution:
	# @param A : list of integers
	# @return an integer
    def solve(self,A):
        A.sort()
        res = -1
        for i in range(0,len(A)):
            if i != len(A)-1 and A[i] == A[i+1]:
                continue
            if A[i] == len(A)-1-i:
                res =1
                break

        return res
    




obj = Solution()
B = [ -4, -2, 0, -1, -6 ]
print(obj.solve(B))