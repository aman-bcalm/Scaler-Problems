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

            row_sum = 0
           

            for j in range(0,len(A[0])):
                row_sum = row_sum + max(A[i][j],  B[i][j])
                

            rs.append(row_sum)
        

        cs = []
        #columns wise sum
        for i in range(0,len(A[0])):

            col_sum = 0
            

            for j in range(0,len(A)):
                col_sum = col_sum + max(A[j][i], B[j][i])
                
            
            
            cs.append(col_sum)
        
        rss, css = 0, 0
        for i in range(0, len(rs)):
            rss += rs[i]
        
        
        for i in range(0,len(cs)):
            css += cs[i]
            

        result = max(rss,css)
        return result

        

        


obj = Solution()
A = [
  [7, 10],
  [6, 5]
]

B = [
  [1, 8],
  [5, 10]
]



print(obj.solve(A,B))