class Solution:

    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        res = [0]
        res = self.ksymb(res,A-1)
        return res[B-1]
        
    
    def ksymb(self,res,A):

        if A == 0:
            return res
        else:
            res1 = []
            i = 0
            while(i < len(res)):
                if res[i] == 1:
                    res1.extend([1,0])
                
                elif res[i] == 0:
                  res1.extend([0,1])
                
                i += 1
                

            return self.ksymb(res1,A-1)
            

obj = Solution()
A = 2
B = 2
print(obj.solve(A,B))


