class Solution:
    # @param A : list of strings
    # @param B : string
    # @return a list of integers
    def solve(self, A, B):
        res = 0
        ir, jr = -1, -1
        for i in range(0, len(A)):
            
            if len(A[i]) >= len(B):
                #print(A[i])
                c = 0
                for j in range(0,len(B)):
                    if A[i][j] == B[j]:
                        c += 1
                    else:
                        break
                
                if c == len(B):
                    if ir == -1:
                        ir = i

                    if jr == -1:
                        jr = i
                    else:
                        jr += 1
                    res += 1
                    
                    #print("*",A[i], res)
        #print(ir,jr,res)
        fres = [ir, jr]
        return fres

obj = Solution()
A = ["a", "b"]
B = "c"
print(obj.solve(A,B))





