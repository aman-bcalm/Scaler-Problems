class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        res = 0
        for i in range (0,len(A)) :
            for j in range (i+1,len(A)):
                if A[i] + A[j] == B :
                    res =1
                    break
            else:
                continue
            break

        return res

obj = Solution()
t = [1,2,2]
sum = 4
print(obj.solve(t,sum))

