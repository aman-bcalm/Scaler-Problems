class Solution:


    def checkBit(self, i, j):

        if (i & 1 << j) >= 1:
            return True
        else:
            return False


	# @param A : list of integers
	# @return a list of list of integers
    def subsets(self, A):

        A.sort()
        res = []
        r1 = []
        res.append(r1)
        #generate eveny subsequence
        for i in range(1,pow(2,len(A))):

             arr = []
             for j in range(0, len(A)):

                 if self.checkBit(i,j):
                     arr.append(A[j])
             res.append(arr)

        res.sort()

        return res

obj = Solution()
A = [15, 20, 12, 19 , 4]
print(obj.subsets(A))

