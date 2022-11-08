class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        ans = []
       
        
        for i in range(0,len(B)):
            lShift = B[i]
            l_in = A.copy()    
            for j in range(0,len(A)):
                l_in[j] = A[(j+lShift) % len(A)]
            
            ans.append(l_in)
        return ans


obj = Solution()
A = [1, 2, 3, 4, 5]
B = [2, 3]
print(obj.solve(A,B))
