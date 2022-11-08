class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
         i = 0
         j = len(A[0]) - 1
         i_res = -1
         j_res = -1      
         while(i <= len(A)-1 and j >= 0 ):
            
             if A[i][j] == B:
                 if i_res == -1 and j_res == -1:
                     i_res = i
                     j_res = j
                 else :
                     if (i + 1) * 1009 + (j + 1) > (i_res + 1) * 1009 + (j_res + 1) :
                         i_res = i
                         j_res = j
                 j -=1 
                     


                 
             elif A[i][j] < B:
                 i += 1
             else:
                 j -= 1

         if i_res != -1 :
             return (i_res + 1) * 1009 + (j_res + 1)
         else :
             return i_res


obj = Solution()
A = [ [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9] ]
B = 2
print(obj.solve(A,B)) 
                 
             
