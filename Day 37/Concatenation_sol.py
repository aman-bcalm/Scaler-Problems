import pandas as pd
def solve(df1, df2):
    # the code for printing the output is already written
    # the code for taking input is already written
    """
    inputs: df1 and df2 are the two dataframes with columns ["chem_score", "phy_score", "Hindi_score"] and
            ["chem_score", "maths_score", "eng_score"] respectively. Basically the two dataframes have
            marks scored by students in two set of tests. These dataframe's indices are the students
            who took the test.
    output: a 2d list where the first element is a list of average marks of subjects for those students who participated in both sets
            and the second element is the list of average marks of students for all the subjects, which are 5 here.
    """
    
    
    ans=[]
    temp=[]
    result4 = pd.concat([df1, df2], axis=1, join="inner")
    result4 = result4.loc[:,~result4.columns.duplicated()]
    column_names=['phy_score', 'Hindi_score', 'chem_score','maths_score','eng_score']
    result4 = result4.reindex(columns=column_names)
    for i in range(0,5):
        temp.append(result4.sum(axis=0)[i]/2)
    ans.append(temp)
    result3 = pd.concat([df1,df2], axis=0, join="outer")
    res = result3.reset_index().drop_duplicates(subset='index',
                                        keep='first').set_index('index')
    temp=[]
    for i in range(0,6):
        temp.append(res.sum(axis=1)[i]/5)
    ans.append(temp)
    return ans
