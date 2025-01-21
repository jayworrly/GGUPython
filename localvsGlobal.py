def spam():
    eggs = 'spam local'
    print(eggs) # This will be printed (4)

def bacon():  #This would be the first call when code is excuted (2)
    eggs = 'bacon local'
    print(eggs)
    spam() # Moving into calling spam (3)
    print(eggs) # 5

eggs = 'global'
bacon() # (1)
print(eggs) #(6)