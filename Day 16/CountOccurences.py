class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        res = 0
        i = 0
        while(i < len(A)):

            if A[i] == 'b' and i + 2 <= len(A)-1:
            
                if A[i:i+3] == "bob":
                    res += 1
                    i += 2
                    continue

            
           
            i += 1
        
        return res

obj = Solution()
A = "rbobobbobljzjdbobbobpncbobobobadbobvlrrbobmypibobbqiycbobdcpbobybobgjqgbobuccboboybobmbob"
print(obj.solve(A))
            

