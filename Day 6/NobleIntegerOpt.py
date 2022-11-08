class Solution:
	# @param A : list of integers
	# @return an integer
    def solve(self,A):
        
        A.sort()
        
        res = -1
        for i in range(0,len(A)):

            gi = -1
            for j in range(i+1,len(A)):
                if A[j] > A[i]:
                    gi = j
                    break

            if gi != -1 and A[i] == len(A) -j :
                res = 1
                break
            elif gi == -1 and A[i] == 0 and len(A)-1-i == 0:
                res = 1
                break
                

        return res




obj = Solution()
B = [ -4, -2, 0, -1, -6 ]
print(obj.solve(B))