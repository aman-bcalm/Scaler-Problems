class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
       
       
       
        sum  = 0
        res = -1
        for i in range(0,len(A)):
            sum = sum + A[i]
            A[i] = sum


        
        for i in range(0,len(A)):
            if i != 0 and i!= len(A)-1:
                if A[i-1] == A[len(A)-1] - A[i]:
                    return i
            
            if i == 0:
                if 0 == A[len(A)-1] - A[i] :
                    return i
        return res


obj = Solution()
A = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
print(obj.solve(A))            
                
                