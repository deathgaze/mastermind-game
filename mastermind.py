################################################################################
# program =     'mastermind'
# version =     '0.01a'
# description = 'play a simple logic guessing game'
################################################################################

import random

def print_title():
    print("\nLet's play...")
    print(\
    r"    ___  ___          _           ___  ____           _  ""\n"\
    r"    |  \/  |         | |          |  \/  (_)         | | ""\n"\
    r"    | .  . | __ _ ___| |_ ___ _ __| .  . |_ _ __   __| | ""\n"\
    r"    | |\/| |/ _` / __| __/ _ \ '__| |\/| | | '_ \ / _` | ""\n"\
    r"    | |  | | (_| \__ \ ||  __/ |  | |  | | | | | | (_| | ""\n"\
    r"    \_|  |_/\__,_|___/\__\___|_|  \_|  |_/_|_| |_|\__,_| ""\n") 

def print_rules():
    print("Rules: I am thinking of a secret 4 digit number. Guess my number.")
    print("- If a digit is in the correct position, I'll mark an O.")
    print("- If one or more of the digits is in my secret, "\
        "but NOT in the correct position, I'll mark an X.")
    print("- If a digit is neither in my secret nor in position, I won't "  \
        "mark anything.")
    print("- If a digit is alredy marked, I will not mark it down again.")

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
        
class MastermindGame:
    guesses = 0
    secret = 
    
    def play_round(self, guess):
        if game_over:
            return 'OOOO'
        
        res = ''
        if guess:
            hit_str = ''
            miss_str = ''
            for i, (g_char, s_char) in enumerate(zip(list(guess), list(secret))):
                if g_char == s_char:
                    # the easy part: finding direct hits
                    hit_str += g_char
                    res += 'O'
            
            for g_char in guess:
                if g_char in secret \
                and g_char not in miss_str \
                and g_char not in hit_str:
                    miss_str += g_char
                    res += 'X'
                
            # Properly format the result before printing it back to the user.
            res = ''.join(sorted(list(res)))
            guesses += 1
        
        if res == 'OOOO':
            self.game_over = True

def play_game():
    print_title()
    print_rules()
    
    while True:

    
    answer = input("Would you like to play again? (y to play again) --> ")
    return answer == 'y'