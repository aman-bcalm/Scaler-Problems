import numpy as np

class Solution: 


    def outlier(self, data):
        '''
        Input:
        data: input data in the form of a python list
        Output:
        ans: return the list of outliers in the form of a python list. If no outliers are present, return an empty list
        '''
        ans = []
        Q1 = np.quantile(data, 0.25)
        Q2 = np.quantile(data, 0.50)
        Q3 = np.quantile(data, 0.75)
        IQR = Q3 - Q1
        UR = Q3 + 1.5*IQR
        LR = Q1 - 1.5*IQR
        for i in range(0, len(data)):
            if LR > data[i] or data[i] > UR:
                ans.append(data[i])

        #print(LR, UR)
        # YOUR CODE GOES HERE



        # Code ends here
        return ans


obj = Solution()
data =  [1, 1, 2, 10, 8, 9, 7, 6, 11, 7, 1, 9, 929, 100]
print(obj.outlier(data))