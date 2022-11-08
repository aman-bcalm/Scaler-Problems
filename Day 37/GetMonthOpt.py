import pandas as pd

class Solution:

    def solve(reg_id, reg_dates):
        """
        Complete the function to return a Pandas Dataframe object as per the description.
        
        """
        res_df = pd.DataFrame(zip(reg_id, reg_dates), columns=["reg_id", "reg_date"])
        res_df["RMonth"] = res_df["reg_date"].apply(lambda x: x.split("-")[1])
        print(res_df["RMonth"])
        return res_df
        
        #pass