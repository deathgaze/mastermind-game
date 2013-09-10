################################################################################
# program =     'mastermind'
# version =     '0.01a'
# description = 'play a simple logic guessing game'
################################################################################

import random

def print_title():
    print(
    )                                                

def format_guess(guess):
    guess = int(guess)
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
def prompt_guess(prompt):
    answer = input(prompt)
    if answer.isdigit() and len(answer) == 4:
        return answer
    elif int(answer) >= 0 and int(answer) < 10000:
        return format_guess(answer)
    else:
        return False

def play_game():
    answer = ''
    secret = str(int(random.random() * 10000))
    guesses = 1
    
    print("I am thinking of a 4 digit number.")
    print("Guess the number.")
    print("If one or more of the digits is in the number I'm thinking of, but "\
        "NOT in the correct position, I'll mark an X.")
    print("If a digit is in the correct position, I'll mark an O.")
    print("If a digit is neither in my number nor in position, I won't mark "  \
        "anything.")
    print("If a digit is alredy marked with an O, I will not mark it down as " \
        "an X.")
    
    while True:
        res = ''
        guess = prompt_guess("Guess #" + str(guesses) + ": ")
        if guess:
            hit_str = ''
            miss_str = ''
            for i, (g_char, s_char) in enumerate(zip(list(guess), list(secret))):
                if g_char == s_char:
                    # the easy part: finding direct hits
                    hit_str += g_char
                    res += 'O'
                elif g_char in secret \
                    and g_char not in hit_str \
                    and g_char not in miss_str:
                    # if its in the secret but we haven't tracked it as either
                    # a hit or a miss, then it's a new miss
                    miss_str += g_char
                    res += 'X'

            print("Result:  ", str('').join(sorted(list(res))))
            guesses += 1
            if res == 'OOOO':
                print("You win! My secret was", secret)
                print("It took you", guesses, "guesses to find my secret.")
                break
        else:
            # Bad Guess
            print("Invalid guess. Guess must be four integers 0-9.")
    
    answer = input("Would you like to play again? (y to play again) --> ")
    return answer == 'y'

print("Let's play Mastermind!")
while play_game():
    continue
    