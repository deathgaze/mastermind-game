################################################################################
# program =     'mastermind'
# version =     '0.01a'
# description = 'play a simple logic guessing game'
################################################################################

import random

def playGame():
    answer = ''
    secret = random.random() * 10000
    print("I am thinking of a 4 digit number.")
    print("Guess the number.")
    print("If one or more of the digits is in the number I'm thinking of, but "+
        "NOT in the correct position, I'll mark an X.")
    print("If a digit is in the correct position, I'll mark an O.")
    
    while True:
        
    
    answer = input("Would you like to play again? (y to play again) --> ")
    return answer == 'y'

print("Let's play Mastermind!")
while playGame():
    continue
    