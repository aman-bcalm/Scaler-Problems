class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        
        op = 0
        ex = -1
        for i in range(0,len(A)):

            if A[i] > B: 
              op += 1
            elif A[i] == B:
              ex = 1
            
                


        
        if ex == 1 :
         return op
        else:
         return ex
