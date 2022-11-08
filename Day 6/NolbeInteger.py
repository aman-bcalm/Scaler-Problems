class Solution:
	# @param A : list of integers
	# @return an integer
	def solve(self, A):
            A.sort()
            res = -1
            for i in range(0,len(A)):

                if A[i] > len(A)-1 - i :
                    continue
                elif res == 1:
                    break
                else :
                    c = 0
                    for j in range(i+1,len(A)):
                        if A[j] > A[i]:
                            c = c +1
                    if c == A[i] :
                        res = 1
                        break
                
            return res




obj = Solution()
A = [1, 1, 3, 3]
print(obj.solve(A))