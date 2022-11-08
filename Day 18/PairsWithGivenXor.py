class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        s = set()
        res = 0
        for i in range(0, len(A)):

            if B ^ A[i] in s:
                res += 1
            s.add(A[i])

        return res

obj = Solution()
A = [3, 6, 8, 10, 15, 50]
B = 5
print(obj.solve(A,B))

