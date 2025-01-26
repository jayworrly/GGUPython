import numpy as np
a = np.array([0.7, 0.75, 1.85, 2.93, 3.05, 2.02, 1.93, 1.62, 1.84, 1.31, 1.39, 0.84])
print(a)
m = np.array(['Jan ', 'Feb ', 'Mar ', 'Apr ', 'May ', 'June ', 'July ', 'Aug ', 'Sept ',  'Oct ', 'Nov ', 'Dec'])
print(m)

print(type(a), type(m), '\n')

combined = []
for i in range(len(a)):
    combined.append([m[i], a[i]])
combined_array = np.array(combined)
reshape_array = combined_array.reshape(12,-1)

print(reshape_array)

mean = np.mean(a)
print('Mean: The average amount of preciptations was: ', mean)

winter = np.array([.7,0.75,0.85])
me = np.mean(winter)
print(winter, me)