import copy

class Solution:


    # @param A : string
    # @return a strings
    def solve(self, A):

        A = list(A)
        res = []
        r_min = [A[0], A[1]]
        for i in range(0, len(A)-1):

            res1 = []
            a1 = A[i]
            rem = A[i+1:len(A)]
            #rem.sort()
            a2 = min(rem)
            res1.append(a1)
            res1.append(a2)
            #res.append(res1)
            if res1 <= r_min:
                r_min = res1
        
        
        #res.sort()
        #f_res = ''.join(res[0])
        f_res = ''.join(r_min)
        return f_res


obj = Solution()
A = "abcdsfhjagj" 
print(obj.solve(A))



