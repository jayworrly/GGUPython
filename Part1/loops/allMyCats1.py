
# creating a list of names
catNames = []
while True:
    print('Enters the name of cat'+ str(len(catNames) +1)+ 
          ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]
print('The cat names are: ')
for name in catNames:
    print("  " + name)