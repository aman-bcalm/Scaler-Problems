class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):

        i = 0
        j = len(A[0])-1
        res = 0
        while i <= len(A)-1 and j >=0 :
            if A[i][j] == 1:
                res = i
                j -= 1
            else :
                i += 1
        return res


obj = Solution()
A = [   [0, 0, 0, 0],
         [0, 1, 1, 1]    ]
print(obj.solve(A))


