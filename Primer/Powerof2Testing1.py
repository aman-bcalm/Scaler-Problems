class Solution:
    # @param A : tuple of integers
    # @return an integer
    def power(self, A):

        nl = []
        for i in range(0,len(A)) :
            nl.append(int(A[i]))

        if sum(nl) <=1:
            return 0
        
        rem = 0
        S = 0
        while((sum(nl[:len(nl):]) > 1 ) and rem == 0):
            for i in range(0,len(nl)):
                
                
                if nl[i] == 0:
                    continue

                



                rem = nl[i] % 2
                nl[i] = int(nl[i]/2)
                
                if rem != 0 and i != len(nl)-1:
                    
                    nl[i+1] = rem*10 + nl[i+1]

            
            
        if rem == 1:
            return 0
        else:
            return 1
      

        




