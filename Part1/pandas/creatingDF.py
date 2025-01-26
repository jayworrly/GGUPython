import pandas as pd
#Creating the array/series
s1 = pd.Series([100,200,300],)
s2 = pd.Series([111,222,333,4444])
# Creating Columns and defing the rows
d = {'first': s1,
     'second': s2}
# Building the DataFrame
df = pd.DataFrame(d)
print(df)

d = {'first' : pd.Series([100, 200, 300], index=['Bill', 'Jane', 'Sue']),
     'second' : pd.Series([111, 222, 333, 4444], index=['Bill', 'Jane', 'Cerill', 'Dancy'])}
df = pd.DataFrame(d)
print(df)
# data frame index
print(df.index)
# data frame columns
print(df.columns)
# create a data frame from dictionary by specific index 
print(pd.DataFrame(d, index=['Dancy', 'Bill', 'Jane']))

data = [{'Alex': 1, 'Joe': 2}, {'Emma': 5, 'Dora': 10, 'Alice': 20}]
print(pd.DataFrame(data))