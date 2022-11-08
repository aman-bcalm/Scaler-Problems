class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):

        i=0
        j=31

        while( j > i):
            n1 = 1<<i
            n2 = 1<<j
            first = (A & n1) >>i
            second = (A & n2) >> j

        
            if( first != second):
                A =  A^(n1)
                A =  A^(n2)

            i+=1
            j-=1
        

        return A


    



obj = Solution()
result = obj.reverse(3)
print(result)
            