class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        len_in = len(A)
        res = []
        if len_in >=2:
            for i in range (0,len(A)-1):
                res.append(A[i+1]-A[i])
        return res
        
       
obj = Solution()
param = [6,2,4,4,3]
solve_res = obj.solve(param)
print(solve_res)
for i in range (0, len(solve_res)):
    print(solve_res[i])