import numpy as np

print ('1-D Array')

x = np.arange(9) #1 Dim-array 0-9
print(type(x)) #Sharing the type of array
print(x, '\n')

print('3x3 array')
a3x3 = x.reshape((3,3)) # Changing the shape of the array to a 3x3 rows by columns 
print(a3x3, '\n')
print (2 ** a3x3) # ndarray are mutable, change elements; exponet with base 2, eg: 2^0, 2^1, 2^2...
print()

print('2x3 array')
a2x3 = np.array([[0,1,2,],[3,4,5]]) # Creating an array 2x3 rows by columns
print(a2x3, '\n')
print(a2x3 + 1)