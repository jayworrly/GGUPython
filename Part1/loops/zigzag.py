import time, sys # This is what we are importing into the program


indent = 0 # We are defining a value to indent
indentIncreasing = True # Wether the indentations is increasing or not

try:
    while True: #This is our main loop
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) #This is telling the program how long it should wait

        if indentIncreasing: 
            # We are now increasing the Indent by 1 until we get to 20
            indent = indent + 1
            if indent == 20:
                indentIncreasing = False
        else:
            # We are now decreasing the Indent by 1 until we get to 0
            indent = indent - 1
            if indent == 0:
                indentIncreasing = True
#This is ending the program
except KeyboardInterrupt:
    sys.exit()