#Importing from the random library
import random

def getAnwser(anwserNumber): #We are defining getAnwser with the parameter of anwserNumber
    if anwserNumber == 1: # We are indicating that if a certain number between 1-9 is hit, these are the outputs that will be shared
        return 'Def could occur'
    elif anwserNumber == 2:
        return 'Highly likely'
    elif anwserNumber == 3:
        return 'Shake gain'
    elif anwserNumber == 4:
        return 'Yes'
    elif anwserNumber == 5:
        return 'No'
    elif anwserNumber == 6:
        return 'Lata'
    elif anwserNumber == 7:
        return 'Thinking ask again'
    elif anwserNumber == 8:
        return 'Not looking to good'
    elif anwserNumber == 9:
        return 'Reply Hazy try again'

r = random.randint(1,9) # we are stating that r is equal to the imported libarary
fortune = getAnwser(r) # we are defing that fortune is equal to the function stated above, with the library we are importing
print(fortune) # we are excuting the code