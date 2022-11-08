import sys

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        #length of array is equal to
        if(B == len(A)):
            return 0


        for i in range(1,len(A)):
            A[i] = A[i-1] + A[i]
        
        res = sys.maxsize
        
        
        C = []
        for i in range(0, len(A) - B+1):
            
            end = i + B - 1
            C_i = []
            if i != 0:
                C_i.append(A[end] - A[i-1])
            else:
                C_i.append(A[end])
            C_i.append(i)
            C.append(C_i)


        for i in range(0,len(C)):
            sm = C[i][0]
            res = min(res,sm)
        
        res_i = -1
        for i in range(0,len(C)):
            if res == C[i][0]:
                res_i = C[i][1]
                break
        
        return res_i



obj = Solution()
A = [ 3, 16, 11, 13, 19, 17, 11, 4, 9, 9, 6, 7, 3, 6, 12, 3, 4, 15, 5, 19 ]
B = 1
print(obj.solve(A,B))

