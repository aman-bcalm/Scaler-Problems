class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        
        AN = 0
        SS = 0
        for i in range(0,len(A)):
            if A[i] == "A":
                AN +=  1
            if A[i] == "G":
                SS += AN
                   
        return SS


obj = Solution()
A = "ABCGAG"
print(obj.solve(A))

