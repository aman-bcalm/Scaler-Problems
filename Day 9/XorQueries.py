class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of list of integers


    #time complexity O(N)
    #algo used calcualte prefix sum for the no of 1s
    #in a subarray if odd no of 1s xor is 1 else xor is 0 
    def solve(self, A, B):

        res = []

        for i in range(1,len(A)):
            if(A[i] == 1):
                A[i] = A[i-1] + A[i]
            else:
                A[i] = A[i-1]

    
        res = []
        for i in range(0,len(B)) :
            stt = B[i][0] - 1
            end = B[i][1] - 1
            
            set = 0
            if(stt != 0) :
                set  = A[end] - A[stt-1]
            else :
                set = A[end]
            
            
            unset = end - stt + 1 - set
            
            x_res = 0
            if set % 2  == 0:
                xor_res = 0
            else:
                xor_res = 1

            res_i = []
            res_i.extend([xor_res,unset])
            res.append(res_i)
        
        

        
        return res


obj = Solution()
A=[1,0,0,0,1]
B=[ [2,4],
    [1,5],
    [3,5] ]

print(obj.solve(A, B))


            
            
                


