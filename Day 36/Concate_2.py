import pandas as pd
import numpy as np

def solve(df1,df2):
    # YOUR CODE GOES HERE
    # just return the 2d list explained in the description
    # the code for printing the output is already written
    # the code for taking input is already written
    ans=[]
    dfc1 = df1["chem_score"]
    dfc2 = df2["chem_score"]
    s = (dfc1.sum() + dfc2.sum()) / 8
    ans.append(s)

    result = pd.concat([df1, df2], axis=1, join='inner')
    av = result.mean(axis=1)
    
    temp = []
    for i in range(len(av)):
        temp.append(av.iloc[i])

    ans.append(temp)
        
        
    


    

    return ans