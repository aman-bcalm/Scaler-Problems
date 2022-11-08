class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        row = len(A)
        col = len(A[0])

        rs = []
        #row wise sum
        for i in range(0,len(A)):

            row_sumA = 0
            row_sumB = 0

            for j in range(0,len(A[0])):
                row_sumA = row_sumA + A[i][j]
                row_sumB = row_sumB + B[i][j]
            
            max_rowSum = max(row_sumA,row_sumB)
            rs.append(max_rowSum)
        

        cs = []
        #columns wise sum
        for i in range(0,len(A[0])):

            col_sumA = 0
            col_sumB = 0

            for j in range(0,len(A)):
                col_sumA = col_sumA + A[j][i]
                col_sumB = col_sumB + B[j][i]
            
            max_colSum = max(col_sumA,col_sumB)
            cs.append(max_colSum)
        
        rss, css = 0, 0
        for i in range(0, len(rs)):
            rss += rs[i]
        
        
        for i in range(0,len(cs)):
            css += cs[i]
            

        result = max(rss,css)
        return result

        

        


obj = Solution()
A = [
    [4, 2],
    [1, 4]
    ]
B = [
  [5, 1],
  [5, 10]
]


print(obj.solve(A,B))