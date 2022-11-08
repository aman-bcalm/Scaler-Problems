import math

class Solution:


    #check if in i the jth biut is set or not
    def checkBit(self, i, j):

        if (i & 1 << j) >= 1:
            return True
        else:
            return False


	# @param A : list of integers
	# @return an integer
    def solve(self, A):

         Sum = 0
        #generate eveny subsequence
         for i in range(1,pow(2,len(A))):

             arr = []
             for j in range(0, len(A)):

                 if self.checkBit(i,j):
                     arr.append(A[j])
            
             mini = min(arr)
             maxi = max(arr)
             Sum += (maxi - mini)
         return Sum


            




