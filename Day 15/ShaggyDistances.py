import sys

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        hmap = {}
        for i in range(0, len(A)):

            if A[i] in hmap:
                hmap[A[i]].append(i)
            else:
                hmap[A[i]] = [i]
        
        ans = sys.maxsize
        for key in hmap:
            if len(hmap[key]) >= 2:
                diff = hmap[key][1] - hmap[key][0]
                ans = min(ans, diff)
        


        if ans != sys.maxsize:
            return ans
        else:
            return -1

obj = Solution()
A = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
print(obj.solve(A))
