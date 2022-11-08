class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        A.sort()
        res = 0 #all elements are the same

        if len(A) == 1:
            return res
        else :
            res = A[1] - A[0]
            for i in range(2, len(A)) :
                diff = abs(A[i] - A[i-1])
                res  = min(res, diff)
            return res


obj = Solution()
A = [5, 17, 100, 11]
print(obj.solve(A))

