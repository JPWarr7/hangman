# installing the global dictionary
# in terminal: pip3 install nltk
#              pip3 install PyDictionary
# in python: import nltk
#            nltk.download()

import random
from PyDictionary import PyDictionary
dictionary = PyDictionary()
from nltk.corpus import words

# generate the random word.
def get_word():
    word_list = words.words()
    word = random.choice(word_list)

    dictionary = PyDictionary()
    definition = dictionary.meaning(word, disable_errors = True)

    while definition is None or len(word) > 10:
        word = random.choice(word_list)
        definition = dictionary.meaning(word, disable_errors = True)

    return word, definition

# create the blanks for the program, shown before each guessing phase and updated with each guess.
def get_blanks(word):
    blanks = []
    word_array = []
    for i in range(len(word)):
        blanks.append('_ ')
        word_array.append(word[i])
    return blanks, word_array

# function to pull the intial setup together and start playing Hangman.
def play_hangman():
    # initial setup
    word, definition = get_word()
    blanks, word_array = get_blanks(word)
    wrong_guesses = []
    guesses = []
    won = False

    # gameplay loop.
    while len(wrong_guesses) < 10 and not won:
        print(f"\n{''.join(blanks)} \nDefinition: {definition} \nGuesses: {guesses} \nWrong Guesses: {wrong_guesses}")
        guess = input('what letter would you like to guess? ')

        # checks to make sure each guess is unique.
        while guess in guesses or guess == '' or len(guess) > 1:
            guess = input(f"Invalid guess! (maybe you already guessed that?) \nGuesses: {guesses}\nWrong Guesses: {wrong_guesses}\nwhat letter would you like to guess? ")

        guesses.append(guess)

        # iterates through the word array to evaluate each character and compare to the guess.
        for i in range(len(word_array)):
            if guess == word_array[i].lower():
                blanks[i] = guess # <- replaces the blank at character[i] with guess, showing your progress toward guessing the word.

        if guess not in word_array: # <- adds to wrong guess if the guess is not in the word.
            wrong_guesses.append(guess)

        if blanks == word_array: # <- once the blanks array is equal to the word, you have won.
            won = True

    if won:
        print(f"{''.join(blanks)}\ncongratulations! you guessed '{word}' in {len(wrong_guesses)} wrong guesses and {len(guesses)} total guesses!")
    
    # if the while loop has finished and won is false, you have exceeded the number of wrong guesses possible and have lost the game.
    else:
        print(f"you lost. the word was '{word}'.")

play_hangman()