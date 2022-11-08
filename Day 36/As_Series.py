import pandas as pd
import numpy as np 

class Solution:

    def solve(self, string):
        """
        returns a series object with word count as values and words as the indices.
        """
        l1 = string.split()
        l1.sort()
        l1 = pd.DataFrame(l1)
        #can also use
        #s1 = l1.iloc[:,0].value_counts()
        s1 = l1.value_counts()
        s1= s1.sort_index()
       
        s1= s1.sort_values()
        return s1

obj = Solution()
st = "How much wood would a woodchuck chuck if a woodchuck could chuck wood"
obj.solve(st)
