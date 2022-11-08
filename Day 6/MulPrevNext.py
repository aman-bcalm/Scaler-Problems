class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        B = []
        if len(A) == 1:
            return A
        else :
            for i in range(0,len(A)):

                if i == 0 :
                    B.append(A[i]*A[i+1])
                elif i == len(A) - 1:
                    B.append(A[len(A)-1] * A[len(A)-2])
                else :
                    B.append(A[i-1]*A[i+1])
        
        return B


obj = Solution()
A  = [0]
print(obj.solve(A))