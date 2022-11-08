class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        
        ala = 26 * [0]
        #ASCII a = 97
        for i in range(0, len(A)) :
            ala[ord(A[i]) - 97] += 1
        
        ala.sort()
        
        i = 0
        while B > 0:
            if B >= ala[i] :
                B = B - ala[i]
                ala[i] = 0
                i += 1
            else :
               B = 0
               ala[i] = ala[i] - B
        
        res = 0
        for i in range(0, len(ala)):
            if ala[i] != 0:
                res +=1
        
        return res




obj = Solution()
A = "abcabbccd"
B = 3 
print(obj.solve(A, B))