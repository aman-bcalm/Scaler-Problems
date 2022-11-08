class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        a_pos1 = []
        pos = 0
        a_pos0 = []

        while(A !=0 ):
            if A & 1 == 1:
                a_pos1.append(pos)
            else :
                a_pos0.append(pos)
            pos +=1
            A = A >> 1
        
        
        a_pos0.reverse()        

        X = 0
        while B != 0 :
            if len(a_pos1) !=0 :
                 pos_toset = a_pos1.pop()
                 X = X | 1 << pos_toset
            elif len (a_pos0) !=0 :
                 pos_toset = a_pos0.pop()
                 X = X | 1 << pos_toset
            else :
                 no_bits = 0
                 temp = X
                 while temp !=0 :
                    temp = temp >> 1
                    no_bits += 1
                 X = X | 1 << no_bits
            
            B -=1
        
        return X


obj = Solution()
print(obj.solve(9,3))
