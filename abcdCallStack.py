def a():  
    print('a() starts') #Starts the stack (1)
    b() # Calls on what we defined b as (2)
    d() # We have now moved back up to A, now going to print out the function called upon (8)
    print('a() returns') #Since D, is finished, it moved back to this (11)

def b():
    print('b() starts') #This is being called on, which is than the second output (3)
    c() #Following our second output, we are now going to call on C (4)
    print('b() returns') # Since all of C code has been excuted, we will print this line out and move back up to A (7)

def c(): 
    print('c() starts') # This will be our third output, since (5)
    print('c() returns') # Since we do not have anything else to call on within the C code, we will print this for our fourth code and move back up (6)

def d():
    print('d() starts') # This was called upon, which will print this out (9)
    print('d() returns') # Since the code is not calling upon anything else, we will print this out (10)

a() # This is excuting the stack