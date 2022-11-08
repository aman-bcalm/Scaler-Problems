import math
class Solution:
    # @param A : list of characters
    # @return a list of characters
    def to_lower(self, A):

        for i in range(0, len(A)) :

            asci = ord(A[i])
            if asci >= 65 and asci <= 90 :
                asci = asci ^ pow(2,5)
            A[i] = chr(asci)
        return A



obj = Solution()
A = [ "S", "c", "A", "L", "E", "r", "A", "c", "a", "D", "e", "m", "y" ]
print(obj.to_lower(A))