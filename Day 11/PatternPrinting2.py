class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):

        res = []
        for i in range(1, A+1):
            res_i = []
            for j in range(1,i+1):
                 res_i.append(j)
            for j in range(0,A-i):
                res_i.append(0)
            res_i.reverse()
            res.append(res_i)
        return res

obj = Solution()
A = 3
print(obj.solve(A))
            

