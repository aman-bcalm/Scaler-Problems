class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        hmap = {}
        for i in range(0, len(A)):

            if A[i] in hmap :
                hmap[A[i]] += 1
            else:
                hmap[A[i]] = 1
        
        res = -1
        for i in range (0, len(A)):

            if hmap[A[i]] >= 2:
                return A[i]
        
        return res


obj = Solution()
A = [6, 10, 5, 4, 9, 120]
print(obj.solve(A))