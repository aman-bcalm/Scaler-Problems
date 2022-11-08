
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : integer
    # @param F : integer
    # @param G : integer
    # @param H : integer
    # @return an integer
    def solve(self, A, B, C, D, E, F, G, H):

        #check all cases when they don't overlap
        
        #lies above 
        if E >= C :
            return 0
        # lies ot the right    
        elif F >= D :
            return 0
        # lies to the bottom
        elif G <= A :
            return 0
        #lies to the right
        elif B >= H :
            return 0
        else :
            return 1



obj = Solution()

A = 0   
C = 4  
E = 2   
G = 6  
B = 0
D = 4
F = 2
H = 6
print(obj.solve(A,B,C,D,E,F,G,H))