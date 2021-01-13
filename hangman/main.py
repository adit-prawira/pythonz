import random
import hangman_art
import hangman_words

#Render logo when starting the program
print(hangman_art.logo)

display = []
word_list = hangman_words.word_list
stages = hangman_art.stages
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
life = len(stages)-1
is_finished = False

#Initialize and render answer by underline, and show initial condition of the hangman
for _ in range(word_length):
    display += "_"

print(" ".join(display))
print(stages[life])

while is_finished == False:
    guess = input("Guess a letter: ")
    for position in range(word_length):
        letter = chosen_word[position]
        if (letter == guess):
            display[position] = letter  
        if(guess not in chosen_word):
            life -= 1
            print(stages[life])
            break
    is_finished = "_" not in display

    print(" ".join(display))

    if(life == 0 and is_finished==False):
        print("You Lose")
        break
    if(life != 0 and is_finished == True):
        print("You Win")
        break

    
