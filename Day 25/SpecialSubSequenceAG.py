
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):

        #count the number of Gs starting from right
        gc = 0
        #count the no of "AG" subsequences
        ss = 0
        for i in range(len(A)-1, -1, -1):
           
            if A[i] == 'G':
                gc += 1
            
            if A[i] == 'A':
                ss += gc

        return ss


obj = Solution()
A = "GAB"
print(obj.solve(A))



