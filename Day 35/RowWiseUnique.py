import numpy as np

class Solution:

    def countfreq(self ,arr2d):
        # YOUR CODE GOES HERE
        # Make sure that you are printing the output matrix simply inside this function.
        # No need to write code to take input
        
        m = len(arr2d)

        res = np.zeros([m,10], dtype = int)
        for i in range(0, len(res)):

            row = np.array(arr2d[i])
            unique, counts =np.unique(row, return_counts=True)

            for j in range(0, len(unique)):

                index = unique[j] - 1
                res[i][index] = counts[j]
        
        res = res.tolist()
        print(res)


obj = Solution()
A = [ [1, 1, 2, 5, 7, 6, 7, 7, 6, 3], 
      [8, 5, 4, 7, 5, 2, 6, 10, 1, 7], 
      [4, 3, 10, 4, 4, 4, 3, 1, 4, 3], 
      [1, 4, 1, 1, 8, 4, 9, 8, 5, 5], 
      [1, 1, 4, 4, 2, 10, 5, 6, 8, 1]]
obj.countfreq(A) 
            

        
