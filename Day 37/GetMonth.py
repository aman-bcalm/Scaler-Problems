import pandas as pd

class Solution:

    def solve(reg_id, reg_dates):
        """
        Complete the function to return a Pandas Dataframe object as per the description.
        
        """
        
        df = pd.DataFrame({"RID": reg_id, "RDate": reg_dates})
        df["RDate"] = pd.to_datetime(df["RDate"])
        df["RYear"] = pd.DatetimeIndex(df["RDate"]).year
        df["RMonth"] = pd.DatetimeIndex(df["RDate"]).month
        df["RDay"] =  pd.DatetimeIndex(df["RDate"]).day
        
        return df
        #pass