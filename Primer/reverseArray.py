class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def solve(self, A):
        rev = []
        for i in range (len(A)-1,-1,-1):
            rev.append(A[i])
        
        return rev



obj = Solution()
test = (1,2,3,4,5)
print(obj.solve(test))