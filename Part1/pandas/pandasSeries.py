import pandas as pd

a = pd.Series(data=[100, 200, 300, 400, 500])
print(a)

a = pd.Series(data=[100, 200, 300, 400, 500], index=['jan', 'feb', 'mar', 'apr', 'may'])
print(a, '\n')
print(a.index, '\n')
print(a['mar'], '\n')

print(a.iloc[[4,3,1]])