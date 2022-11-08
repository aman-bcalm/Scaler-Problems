class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        arr = []
        arr.extend([A,B,C])
        arr.sort()
        res = 0
        base = 0

        for i in range(len(arr)-1,-1,-1):
            res = res + arr[i] * pow(10,base)
            base += 2
        return res

        
obj = Solution()
obj.solve(55,43,47)