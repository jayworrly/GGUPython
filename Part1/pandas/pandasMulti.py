import pandas as pd

a = pd.DataFrame(columns=['Days_of_Week', 'hours'],
                 data=[['Mon', 40], ['Tue', 20],
                       ["Wed", 30],  ["Thurs", 0.0],
                        ["Friday", 45]
                        ])
print(a, '\n')
# Describe adds in mean, median, std, quartiles, min/max

print(a.describe())

a.to_csv('hoursworked.csv', index= False)

df = pd.read_csv('hoursworked.csv', delimiter= ',')
print(df)