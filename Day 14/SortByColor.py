class Solution:
    # @param A : list of integers
    # @return a list of integers
    def sortColors(self, A):
        
        c0, c1, c2 = 0, 0, 0
        for i in range(0, len(A)):
            if A[i] == 0:
                c0 += 1
            elif A[i] == 1:
                c1 += 1
            else :
                c2 += 1
        
        A = []
        for i in range(0,c0) :
            A.append(0)
        for i in range(0,c1):
            A.append(1)
        for i in range(0,c2):
            A.append(2)
        
        return A

        


obj = Solution()
A = [0, 1, 2, 0, 1, 2]
print(obj.sortColors(A))
