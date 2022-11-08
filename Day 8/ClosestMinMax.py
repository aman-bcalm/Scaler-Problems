import math
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        mi = A[0]
        mn_i = []
        ma = A[0]
        ma_i = []
        
        for i in range(0,len(A)):
            if A[i] > ma:
                ma = A[i]
               
            if A[i] < mi:
                mi = A[i]

        for i in range(0,len(A)):
            if A[i] == ma:
                ma_i.append(i)
               
            if A[i] == mi:
                mn_i.append(i)
                
        print(mn_i,ma_i)
        lsa = abs(mn_i[0]-ma_i[0])
        for i in range(0,len(mn_i)):
            for j in range(0,len(ma_i)):
                 print(mn_i[i], ma_i[j], abs(mn_i[i]-ma_i[j]))
                 if lsa > abs(mn_i[i]-ma_i[j]):
                     lsa = abs(mn_i[i]-ma_i[j])

        #since end-start+1 is the subarray length
        lsa = lsa+1        
        
        return lsa


obj = Solution()
A = [ 814, 761, 697, 483, 981 ]
print(obj.solve(A))
