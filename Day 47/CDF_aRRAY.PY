import numpy as np

class Solution :

    def cdf(data):
        '''
        input:
        data: the input python list to calculate the cdf of
        output:
        cdf_arr: return the resultant cdf array of the provided data, in numpy.ndarray type
        '''

        hist, bin_edges = np.histogram(data, bins =  10, density = True)
        hist_n = hist / hist.sum()
        cdf_arr = np.cumsum(hist_n)
        # YOUR CODE GOES HERE.
        
        # Your code ends here
        return cdf_arr


obj = Solution()


