class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        ans = []
       
        
        for i in range(0,len(B)):
            k = B[i]
            if k > len(A):
                k = k % len(A)
            AR = A[::-1]    
            AR = AR[0:len(A)-k:1][::-1] + AR[len(A)-k:len(A):1][::-1]
            ans.append(AR)
        return ans

obj = Solution()
A = [ 4, 74, 35, 16, 100, 77, 50, 51, 31, 29, 67, 12, 43, 31, 83, 2, 85, 85, 39, 27, 64, 86, 5 ]
B = [ 73, 70, 47, 19, 46, 25, 46, 4, 33, 33, 6, 31, 23, 19, 44, 53, 69, 30, 69, 89, 59, 25, 38, 82, 26, 8, 36, 3 ]
print(obj.solve(A,B))