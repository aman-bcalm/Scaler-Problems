class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        A = list(A)
        i , j = 0 , len(A) -1
        while i < j:
            t = A[i]
            A[i] = A[j]
            A[j] =  t
            i += 1
            j -= 1
        
        A = ''.join(A)
        return A

obj = Solution()
A = "scaler"
print(obj.solve(A))
