import pandas as pd
import numpy as np
def solve(df):
    """
    input: pandas dataframe with columns ['Date', 'R_id', 'Phy', 'Chem', 'Math']
    output: pandas series
    """
    
    # code for taking input and printing output is already taken care of just return the list with required elements.
    """
        You need to return a series where the elements will be the most occuring month,
        most occuring month's frequency, average chemistry,physics and maths marks in 
        most occuring months upto two decimal places in this order.
    """
    # YOUR CODE GOES HERE
    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.strftime('%B')
    sr =  df["Month"].value_counts()
    freq = sr.iloc[:1].values[0]
    mi = sr.sort_index()
    mt = mi[mi.values == freq].index[0] 
    mtr = mt[0:3].upper()
    df1 = df.set_index("Month")
    c = round(df1.loc[mt]["Chem"].mean(),2)
    p = round(df1.loc[mt]["Phy"].mean(),2)
    m = round(df1.loc[mt]["Math"].mean(),2)

    return pd.Series([mtr, freq, c, p, m])