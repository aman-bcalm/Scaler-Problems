class Solution:
    # @param A : list of characters
    # @return an integer
    def solve(self, A):

        res = 1
        for i in range(0, len(A)):

            asci = ord(A[i])
            if (asci >=65 and asci <= 90) or (asci >= 97 and asci <= 122):
               continue
            else :
                res = 0
                break
        return res

obj = Solution()
A = ['S', 'c', 'a', 'l', 'e', 'r', '#', '2', '0', '2', '0']
print(obj.solve(A))

