import random
import hangman_word
import hangman_stages
# word_list = ["apple","beautiful","potato"]
lives = 6
# chosen_word = random.choice(word_list)
chosen_word = random.choice(hangman_word.words)
print(chosen_word)
display = []
# for letter in chosen_word:
#     display += "_"
# print(display)
for i in range(len(chosen_word)):
    display += '_'
print(display)
game_over = False
while not game_over:
    gusses_letter=input("guess a letter : ").lower()
    # for letter in chosen_word:
    for position in range(len(chosen_word)):
         letter = chosen_word[position]
         if letter == gusses_letter:
             display[position]=gusses_letter
    print(display)
    if gusses_letter not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("you lose")
    if '_' not in display:
        game_over=True
        print("you win")
    print(hangman_stages.stages[lives])
