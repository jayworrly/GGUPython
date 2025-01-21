def spam(divideBy): # This is defining the function
    try: #This is an error handling clause, if we have a feeling an error will occur
        return 42 / divideBy # The purpose is to divide a number by 42
    except ZeroDivisionError: # this is the error we are expecting, which we are asking python to move past if it occurs
        print('Invalid argument')
print(spam(2)) # Within the second parathesis are we giving "divideby" a value
print(spam(12))
print(spam(0))
print(spam(1))