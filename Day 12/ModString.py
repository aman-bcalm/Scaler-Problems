class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def findMod(self, A, B):
        
        res = 0
        tpi = 1
        for i in range(len(A)-1,-1,-1):
            #power of 10
            tp = len(A) - 1 - i
            if i !=  len(A)-1:
                tpi = (tpi *10)% B


            digit = int(A[i]) % B
            res = (res + (digit * tpi) % B) %B

        return res
           
    
