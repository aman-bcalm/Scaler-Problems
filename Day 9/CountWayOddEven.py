class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        #build prefix sum odd and even arrays
        e_s = []
        e_s.append(A[0])
        o_s = []
        o_s.append(0)

        for i in range(1,len(A)) :
            if i % 2 == 0 :
                t = e_s[i-1] + A[i]
                e_s.append(t)
                o_s.append(o_s[i-1])

            else :
                t = o_s[i-1] + A[i]
                o_s.append(t)
                e_s.append(e_s[i-1])
        
        cnt  = 0
        n = len(A)
        for i in range(0,n) :
            
            if i == 0 :
                if (e_s[n-1] - e_s[0]) == (o_s[n-1] - o_s[0]):
                    cnt += 1
            elif i == n-1 :
                if e_s[n-2] == o_s[n-2]:
                    cnt += 1
            else :
                if e_s[i-1] + (o_s[n-1] - o_s[i]) == o_s[i-1] + (e_s[n-1] - e_s[i]):
                    cnt += 1
        
        return cnt
        




obj = Solution()
B = [1,1,1]
print(obj.solve(B))

