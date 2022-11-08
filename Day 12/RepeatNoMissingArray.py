class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        
       
        f_A = [0 for i in range(0,len(A))]
        for i in range(0,len(A)):
            index = A[i] - 1
            f_A[index] += 1
            
        
        
        d_A = 0
        m_A = 0
        for i in range(0,len(A)):
            if f_A[i] == 2:
                 d_A = i+1

            if f_A[i] == 0:
                 m_A = i+1
        
        res = []
        res.append(d_A)
        res.append(m_A)
        return res

            

        
       

obj = Solution()
A = [3, 1, 2, 5, 3]
print(obj.repeatedNumber(A)) 



        