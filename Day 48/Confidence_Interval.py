
import numpy as np

class Solution:

    

    

    def ciList(self, data):
        '''
        input: data -> Variable containing the input data in form of python list
        output: res -> A list of list variable with each internal list containing the required confidence interval in the order of 68%, 95%, and 99%
        '''

        res = []
        m = np.mean(data)
        z1 = 1
        n = len(data)
        st = np.std(data)
        m_err1 = (st * 1) / n**(1/2)
        m_err2 = (st * 1.96) / n**(1/2)
        m_err3 = (st * 2.57) / n**(1/2)
        u1 = round(m-m_err1, 2)
        v1 = round(m+m_err1, 2)
        u2 = round(m-m_err2, 2)
        v2 = round(m+m_err2, 2)
        u3 = round(m-m_err3, 2)
        v3 = round(m+m_err3, 2)
        c1 = [u1, v1]
        c2 = [u2, v2]
        c3 = [u3, v3]
        res.extend([c1, c2, c3])

        return res


obj = Solution()
data = [2, 3, 5, 6, 7, 9, 8, 1, 2]
print(obj.ciList(data))
       
        
        
        
    