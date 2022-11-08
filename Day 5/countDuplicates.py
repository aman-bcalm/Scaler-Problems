class Solution:
    # @param A : tuple of integers
    # @return an integer
    def solve(self, A):
        
        c = 0
        for i in range(0,len(A)):
            for j in range (i+1,len(A)):
                if(A[i] == A[j]):
                    c += 1
                    break
        return c
        

