
class Solution:

 def eleCount(self, x, A):
        c = 0
        for i in range(0,len(A)):
            if x == A[i]:
                c += 1
        #print(c, int(len(A)/3), (int(len(A)/3) + 1))
        if c >= (int(len(A)/3) + 1) :
            return 1
        else :
            return -1


    # @param A : tuple of integers
    # @return an integer
 def repeatedNumber(self, A):

        #frequency counter then number
        fc1 = 0
        fc1_n = None
        fc2 = 0
        fc2_n = None

        for i in range(0,len(A)):
            if i == 0:
                fc1 = 1
                fc1_n = A[0]
            else :
                if A[i] == fc1_n :
                    fc1 += 1
                elif A[i] == fc2_n:
                    fc2 += 1
                else :
                    if fc1 == 0:
                        fc1 = 1
                        fc1_n = A[i]
                    elif fc2 == 0:
                        fc2 = 1
                        fc2_n = A[i]
                    else:
                       
                        fc1 -= 1
                        if fc1 == 0:
                            fc1_n = None
                        fc2 -= 1
                        if fc2_n == 0:
                            fc2_n = None
            
        #print(fc1,fc1_n, fc2, fc2_n)
        if fc1 > 0 and fc1 >= fc2:
            #print(self.eleCount(fc1_n,A))
            if self.eleCount(fc1_n,A) == 1:
                return fc1_n
        if fc2 >  0 and fc2 >= fc1:
            if self.eleCount(fc2_n,A) == 1:
                return fc2_n
        
        return -1

    
        
        


obj = Solution()
A = [1,1,1,1,1,2,3,4,5,6,7,8]

print(obj.repeatedNumber(A))



