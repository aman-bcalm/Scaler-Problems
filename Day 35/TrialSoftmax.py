import numpy as np

class Solution:


    def softmax(self, data):

        data = np.array(data)
        d1 = np.exp(data)
        es = np.sum(d1)

        for i in range(0, len(d1)):

            d1[i] = d1[i] / es

        d1 = np.round(d1, decimals=3)
        print(d1)


obj = Solution()
A = [6,7,5,18,1,12,7,18,19,10,19,9,0,17,9,8,15,14,8,10,3,3,7,17,19,13,5,18,18,15,3,12,14,11,3,10,2,18,12,5]
obj.softmax(A)