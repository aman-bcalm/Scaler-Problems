class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def solve(self, A, B):

        j = 0
        c_c = A[j]
        found = False

        for i in range(0, len(B)):

            if B[i] == c_c:
                j += 1
                if j == len(A):
                    found = True
                    break
                else:
                    c_c = A[j]
            
    
        
        if found:
            return "YES"
        else:
            return "NO"

obj = Solution()
A = "apple"
B = "appel"
print(obj.solve(A, B))


