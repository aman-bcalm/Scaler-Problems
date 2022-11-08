class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):

        res = []
        for i in range(0,A):
            res.append(0)
       
        for i in range(0,len(B)):

                start = B[i][0]-1
                end = B[i][1]-1
                don = B[i][2]
                res[start] = (res[start] + don)
               
                if end+1 != A:
                    res[end+1] = res[end+1] - don
        
      
        sum = 0
        for i in range(0,A):
            sum = sum + res[i]
            res[i] = sum

        return res
            




obj = Solution()
N = 5 
D = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
print(obj.solve(N,D))
