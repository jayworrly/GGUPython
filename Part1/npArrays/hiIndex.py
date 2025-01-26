supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
print(supplies.index('pens'))
print(supplies.append('staplers'))

for index, item in enumerate(supplies):
    print('Index ' + str(index), 'in supplies is: ' + item)

