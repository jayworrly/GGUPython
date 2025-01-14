# This is a number guessing game

import random
secretNumber = random.randint(1,100)
print('I am thinking of a number between 1 and 100.')

# We are going to ask the player to guess six times

for guessesTaken in range(1,7):
    print("Take a guess.")
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is to low.')

    elif guess > secretNumber:
        print('Your guess is to high.')
    else:
        break # This means it has guessed party has guess the correct anwser

if guess == secretNumber:
    print('WINNER! You have guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('LOSER, The number I was thing of was ' + str(secretNumber))
