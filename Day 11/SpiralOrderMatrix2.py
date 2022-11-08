class Solution:
	# @param A : integer
	# @return a list of list of integers
	def generateMatrix(self, A):
         
         res = []
         for i in range(0,A):
            res_i = []
            for j in range(0,A):
                res_i.append(-1)
            res.append(res_i)
        


         top = 0
         right = A-1
         bottom = A-1
         left = 0
         k = 1
         while (top <= bottom and left <= right):
            for i in range(left, right+1):
                res[top][i] = k
                k += 1
            top += 1
            for i in range(top,bottom+1):
                res[i][right] = k
                k += 1
            right -= 1
            for i in range(right,left-1,-1):
                res[bottom][i] = k
                k += 1
            bottom -= 1
            for i in range(bottom, top-1,-1):
                res[i][left] = k
                k += 1
            left += 1

         return res
         
         



         

obj = Solution()
print(obj.generateMatrix(80))

