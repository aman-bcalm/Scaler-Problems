class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        N = len(A)

        i  , j = 0, 0
        res = []
        while(i<N and j<N):
            i1 = i
            j1 = j
            res_i = []
            while(i1<N and j1>=0):
                res_i.append(A[i1][j1])
                i1 += 1
                j1 -= 1

            res.append(res_i)

            if j == N-1:
                i += 1
            else:
                j += 1
        
        for i in range(0,len(res)):
            # no of 0s
            nzs = N - len(res[i])
            for j in range(0,nzs):
                res[i].append(0)
        

        return res


obj = Solution()
A = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
print(obj.diagonal(A))

