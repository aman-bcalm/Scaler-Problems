class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        #prefix sum array
        st = {}
        sumt = 0
        res = 0 
        for i in range(0, len(A)):
            sumt += A[i]
            
            if sumt == 0 or sumt in st:
                res = 1
                break
            else:
                st[sumt] = i
        
        return res 



       
        
        

obj = Solution()
A = [1, 2, 0, 4, 5]
print(obj.solve(A))

