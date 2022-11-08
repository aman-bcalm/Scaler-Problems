class Solution:


    # @param A : string
    # @return an integer
    def solve(self, A):
    
        A = list(A)
        for i in range(0, len(A)):
            A[i] = ord(A[i])
        
        e_l = []
        o_l = []
        for i in range(0, len(A)):

            if A[i] % 2 == 0:
                e_l.append(A[i])
            else:
                o_l.append(A[i])
        
        e_l.sort()
        o_l.sort()
        res = e_l + o_l
        #print(res)
        for i in range(0, len(res)-1):

            if abs(res[i] - res[i+1]) == 1:
                #print(res[i], res[i+1])
                return 0
        
        return 1
        #print(e_l)
        #print(o_l)
        #print(res)

obj = Solution()
A ="aab"
print(obj.solve(A))


