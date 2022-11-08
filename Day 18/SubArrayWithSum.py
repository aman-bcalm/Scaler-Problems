class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):

        hmap = {}
        sum  = 0
        res = [-1]
        res_f = [-1]
        for i in range(0, len(A)):

            sum = sum + A[i]
            hmap[sum] = i
            if sum == B :
                res = [0,i]
                res_f = A[0:i+1]
                break
            elif sum - B in hmap:
                #print("executing break", hmap, sum-B)
                res = [hmap[sum-B]+1, i]
                res_f = A[hmap[sum-B]+1: i+1]
                break
            
        return res_f

obj = Solution()
A = [5, 10, 20, 100, 105]
B = 110
print(obj.solve(A,B))

      



