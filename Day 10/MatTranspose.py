class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        
        #square matrix
        if len(A) == len(A[0]):
            for i in range(0, len(A)):
                for j in range(i+1, len(A[i])):
                    a = A[i][j]
                    b = A[j][i]
                    a = a ^ b
                    b = a ^ b
                    a = a ^ b
                    A[i][j] = a 
                    A[j][i] = b 
            return A
        #rectangular matrix
        else:
            res = []
            for j in range(0,len(A[0])):
                res_i = []
                for i in range(0,len(A)):
                    res_i.append(A[i][j])
                res.append(res_i)
            return res
            


        


obj = Solution()
A =[
  [21, 62, 16, 44, 55, 100, 16, 86, 29],
  [62, 72, 85, 35, 14, 1, 89, 15, 73],
  [42, 44, 30, 56, 25, 52, 61, 23, 54],
  [5, 35, 12, 35, 55, 74, 50, 50, 80],
  [2, 65, 65, 82, 26, 36, 66, 60, 1],
  [18, 1, 16, 91, 42, 11, 72, 97, 35],
  [23, 57, 9, 28, 13, 44, 40, 47, 98]
]
print(obj.solve(A))
