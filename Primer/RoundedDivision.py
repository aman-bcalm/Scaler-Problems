
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        res = (float(A)/200)
        deci = abs(float(int(res) - res))
        if res < 0 and deci == 0.5:
            res = res - 0.5
        elif res > 0 and deci == 0.5:
            res = res + 0.5
        else :
            
            res = round(res)
        
        res = int(res)
        return res
        


obj = Solution()
print(obj.solve(500))

