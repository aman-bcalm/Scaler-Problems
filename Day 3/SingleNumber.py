class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        N = len(A)
        ans1 = 0
        for i in range (0,N):
            ans1 = ans1 ^ A[i]
        
        atemp = ans1

        k = 0
        atemp = atemp ^ (atemp & (atemp-1))
        print(atemp)
        while atemp !=0:
            k+=1
            atemp = atemp >> 1
        print(k)
        sn1 , sn2 = 0 , 0
        for i in range (0,N):

            if A[i] & (1 << k-1) == 0:
                sn1 = sn1 ^ A[i]
            else :
                sn2 = sn2 ^ A[i]


        res = [sn1, sn2]
        res.sort()
        return res



        
    



obj = Solution()
arr = [ 186, 256, 102, 377, 186, 377 ]
print(obj.solve(arr))
