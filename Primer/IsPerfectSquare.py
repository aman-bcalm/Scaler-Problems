class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        result = 0

        if A == 1:
            return 1

        upper_Bound = int((A+1)/2)

        for i in range (2,upper_Bound):

            if i*i == A:
             result += 1
             break
        
        
        return result


obj = Solution()
print(obj.solve(121))