################################################################################
# program =     'mastermind'
# version =     '0.01a'
# description = 'play a simple logic guessing game'
################################################################################

import random

def formatGuess(guess):
    if guess < 10:
        return "000" + str(guess)
    elif guess < 100:
        return "00" + str(guess)
    elif guess < 1000:
        return "0" + str(guess)
    else:
        return str(guess)

# Takes a prompt and returns a formatted guess as a string. Returns false
# if the user enters invalid input
def promptGuess(prompt):
    answer = input(prompt)
    if answer.isdigit() and len(answer) == 4:
        return answer
    elif int(answer) >= 0 and int(answer) < 10000:
        return formatGuess(answer)
    else:
        return False

# Takes a guess and secret and returns a string containing an 'O' for every
# element in guess that equals the corresponding element in secret
def getHits(guess, secret):
    res = ''
    for i, j in zip(guess, secret):
        if i == j:
            res.append('O')
    return res
    

# Takes the hits, guess and secret. Returns a string containing an 'X' for every digit
# in 
def getMisses(hits, guess, secret):
    return 'X'

def playGame():
    answer = ''
    secret = random.random() * 10000
    guesses = 1
    print("I am thinking of a 4 digit number.")
    print("Guess the number.")
    print("If one or more of the digits is in the number I'm thinking of, but "+
        "NOT in the correct position, I'll mark an X.")
    print("If a digit is in the correct position, I'll mark an O.")
    print("If a digit is neither in my number nor in position, I won't mark "
        "anything.")
    
    while True:
        res = ''
        guess = promptGuess("Guess #" + guesses + ": ")
        if guess:
            # We got a valid guess
            res.append(getHits(guess, secret))
            res.append(getMisses(res, guess, secret))
            print(res)
            guess += 1
            if res == 'OOOO':
                print("You win! My secret was", secret)
                break
        else:
            # Bad Guess
            print("Invalid guess. Guess must be four integers 0-9.")
    
    answer = input("Would you like to play again? (y to play again) --> ")
    return answer == 'y'

print("Let's play Mastermind!")
while playGame():
    continue
    