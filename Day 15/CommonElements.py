class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):

        hmap = {}
        for i in range(0, len(A)):

            if A[i] in hmap:
                hmap[A[i]] += 1
            else:
                hmap[A[i]] = 1

        hmap1 = {}
        for i in range(0, len(B)):

            if B[i] in hmap1:
                hmap1[B[i]] += 1
            else:
                hmap1[B[i]] = 1
        res = []
        for key1 in hmap:
            
            if key1 in hmap1:
                n_times = min(hmap[key1], hmap1[key1])
                res.extend(n_times * [key1])
        
        return res
                


obj = Solution()
A = [2, 1, 4, 10]
B = [3, 6, 2, 10, 10]
print(obj.solve(A, B))
