import math

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):

        res = 0
        tpi = 1
        for i in range(len(A)-1,-1,-1):
            #power of 10
            tp = len(A) - 1 - i
            if i !=  len(A)-1:
                tpi = (tpi *10)% 8


            digit = int(A[i]) % 8
            res = (res + (digit * tpi) % 8) %8
           
        

        if res == 0:
            return 1
        else:
            return 0

obj = Solution()
A = "123"
print(obj.solve(A))



