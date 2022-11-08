class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):

        A_r = len(A)
        A_c = len(A[0])
        B_r = len(B)
        B_c = len(B[0])

      
        res = []
        for i in range(0,A_r):
            res_i = []
            for j in range(0,B_c):
                S = 0
                for k in range(0,A_c):
                   S += A[i][k] * B[k][j]
                res_i.append(S)
            res.append(res_i)
        
        return res
                


obj = Solution()
A = [[1, 2], [3,4]] 
B = [[5, 6], [7,8]] 
print(obj.solve(A,B))