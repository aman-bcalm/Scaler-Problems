class Solution:

    def isPalindrome(self,s1,s2,A):
        res = 1
        while (s1>= 0 and s2 < len(A)) and A[s1] == A[s2]:
            s1 -= 1
            s2 += 1
        
        return s1 == -1 and s2 == len(A)
    
    def giveNextNo(self, A):

        #last digit
        ld = A[len(A)-1]
        ld = int(ld)
        if ld < 9:
            ld = ld + 1
            A[len(A)-1] = str(ld)
        else : #
            carry = 1
            for i in range(len(A)-1, -1,-1):
               d = int(A[i])
               A[i] = str((d + carry) % 10)
               carry = int((d + carry) / 10)
              
            if carry == 1:
                A.insert(0,"1")
     
        return A.copy()

               

    # @param A : string
    # @return a strings
    def solve(self, A):
        A = list(A)
       
        B = self.giveNextNo(A)

        while (True):

            s2 = int(len(B)/2)
            s1 = int(len(B)/2) - 1
       
      
            if (self.isPalindrome(s1,s2,B) or self.isPalindrome(s2,s2,B)):
                    break
            else:
                B = self.giveNextNo(B)
             
        
        B = ''.join(B)
        return B


obj = Solution()
A = "1740948824551711527614232216857618927954312334113874277931986502860248650900613893446066184963788291"

print(obj.solve(A))

               


        


