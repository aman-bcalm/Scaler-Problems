class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):

        hmap = {}
        for i in range(0, len(A)):
            
            if A[i] in hmap :
                hmap[A[i]] += 1
            else :
                hmap[A[i]] = 1
            
        if len(hmap.keys()) == 1:
            return 1
        else :
            even_t = 0
            even_n = 0
            odd_t =0
            odd_n = 0
            for key in hmap.keys():

                if hmap[key] % 2 == 0:
                    even_t += hmap[key]
                    even_n += 1
                else:
                    odd_t += hmap[key]
                    odd_n += 1
            
            if odd_n > 1 :
                return 0
            else:
                return 1


obj = Solution()
A = "abbaee"
print(obj.solve(A))


