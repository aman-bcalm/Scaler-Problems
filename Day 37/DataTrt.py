import pandas as pd
import numpy as np
df= pd.read_csv('input_data.csv')
df.fillna(0, inplace = True)
df.replace(-np.inf, -1, inplace = True)
df.replace(np.inf, 1, inplace = True)
df['dataPoints'] = round(df['dataPoints']**(1/2),2)
df.to_csv('output_data.csv')
