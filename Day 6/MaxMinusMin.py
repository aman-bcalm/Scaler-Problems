class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        A.sort()
        res = A[len(A)-B] - A[B-1]
        return res

obj = Solution()
A = [ 34, 7, 96, 37, 12, 13, 22, 86, 17, 78, 95, 61, 42, 1, 42, 58, 98, 78, 92, 85, 10, 97 ]
B = 22
print(obj.solve(A,B))
