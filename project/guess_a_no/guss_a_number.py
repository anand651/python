import random
import guesses_logo
EASY_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTEMPTS=5

def set_difficulty(level_chosen):
    if level_chosen=='easy':
        return EASY_LEVEL_ATTEMPTS
    elif level_chosen=='hard':
        return HARD_LEVEL_ATTEMPTS
    else:
        return

def check_answer(guessed_number,answer,attempts):
    if guessed_number<answer:
        print("your guess is too low")
        return attempts-1
    elif guessed_number>answer:
        print("youe guess is too high")
        return attempts-1
    else:
        print(f"your guess is right... the answer was {answer}")

def game():
    print(guesses_logo.lojo)
    print("let me think of a number between 1 to 50")
    answer=random.randint(1,50)
    print(answer)
    level=input("choose level of difficulty... type 'easy' or 'hard' :")
    attempts=set_difficulty(level)
    if attempts != EASY_LEVEL_ATTEMPTS and attempts != HARD_LEVEL_ATTEMPTS:
        print("you have enter wrong difficulty level play again")
        return
    guessed_number=0
    while guessed_number!=answer:
        print(f"you have {attempts} attempts remaining to guess a number")
        guessed_number=int(input("guess the number"))
        attempts=check_answer(guessed_number,answer,attempts)
        if attempts==0:
            print("you are out of guesses... you lose!")
            return
        elif guessed_number!=answer:
            print("guess again")

game()