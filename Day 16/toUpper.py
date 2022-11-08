import math
class Solution:
    # @param A : list of characters
    # @return a list of characters
    def to_upper(self, A):

        for i in range(0, len(A)) :

            asci = ord(A[i])
            if asci >= 97 and asci <= 122 :
                asci = asci ^ pow(2,5)
            A[i] = chr(asci)
        return A

obj = Solution()
A = ['S', 'c', 'a', 'L', 'e', 'R', '#', '2', '0', '2', '0']
print(obj.to_upper(A))