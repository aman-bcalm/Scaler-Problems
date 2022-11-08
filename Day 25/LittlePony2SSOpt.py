import copy

class Solution:


    # @param A : string
    # @return a strings
    def solve(self, A):

        A = list(A)
        res = ""
        l_e = A[0:len(A)-1]
        m1 = min(l_e)
        l_eStr = ''.join(l_e)
        i = l_eStr.find(m1)
        
        #find the minimum in the remaining list i.e. i+1 to len(A)-1
        l_s = A[i+1:len(A)]
        m2 = min(l_s)
        res = m1 + m2
        return res


obj = Solution()
A = "ksdjgha" 
print(obj.solve(A))
