class Solution:
    # @param A : list of strings
    # @param B : string
    # @return an integer
    def solve(self, A, B):

        hmap = {}
        for i in range(0, len(B)):
            hmap[B[i]] = i
        #print(hmap)

        res = 1
        for i in range(0,len(A)-1):

            s1 = A[i]
            s2 = A[i+1]
            l1 = len(s1)
            l2 = len(s2)
            j = 0
            while(l1 > 0 and l2 > 0):
                
                #lexographically greter
                if hmap[s1[j]] > hmap[s2[j]]:
                    res = 0
                    break
                #smaller no need to check other characters
                elif hmap[s1[j]] < hmap[s2[j]]:
                    break
                #equal we need to move to the next character for comparison
                else:
                    j += 1
                    l1 -= 1
                    l2 -= 1
            
            if res == 0:
                break
            else:
                if l1 > l2 and  s2 in s1:
                    res = 0
                    break
        
        return res






A = ["fine", "none", "no"]
B = "qwertyuiopasdfghjklzxcvbnm"

obj = Solution()
print(obj.solve(A,B))