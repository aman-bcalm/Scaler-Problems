class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        A.sort()

        for i in range(0, len(A)):
            S = 0

            for j in range(i, len(A)):
                S += A[j]

                if S == B:
                    return 1
        
        return 0

obj = Solution()
A = [2,2,2,2]
B = 5
print(obj.solve(A, B))


