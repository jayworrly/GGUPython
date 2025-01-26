supplies = ['pens', 'staplers', 'flamethrowers', 'binders']

# For loop, length of supplies is being picking up a number
for i in range (len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

# I like this way
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']

for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supplies is: ' + item)

