class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):

        #cocatenate string with itself
        A += A

        #delete all uppercase letters
        A = list(A)
        for i in range(len(A) - 1, -1, -1) :

            if  65 <= ord(A[i]) and 90 >= ord(A[i]) :
                del A[i]
        
        vowels = ['a','e','i','o','u']
        for i in range(0, len(A)):

            if A[i] in vowels:
                A[i] = "#"
        
        A = ''.join(A)
        return A


obj = Solution()
A="AbcaZeoB"
print(obj.solve(A))




