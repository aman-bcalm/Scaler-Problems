class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def getSum(self, A, B, C):

        hmap = {}
        for i in range(0, len(C)):
            
            if C[i] in hmap :
                hmap[C[i]] += 1
            else :
                hmap[C[i]] = 1
            
        Sum = 0
        count = 0
        for key in hmap.keys():
            if hmap[key] == B:
                Sum += key
                count += 1

        if count == 0:
            return -1
        else:
            return Sum

obj = Solution()
N=5 
K=2 
A=[1, 2, 2, 3, 3]
print(obj.getSum(N,K,A))
