class Solution:

    def solve(self, A):
            A.sort()
            start = A[0]
            sorted = 1
            for i in range (1,len(A)) :
                if A[i] != start+1 :
                    sorted = 0
                    break
                else :
                    start = A[i]
            return sorted       



obj = Solution()
B = [1,2,3,5]
print (obj.solve(B))