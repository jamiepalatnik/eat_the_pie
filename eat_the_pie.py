import random

def main():
    print("Welcome to Eat the Pie!")

    word_list = ["recurse", "apple", "programming", "lists", "python", "games", "sustainable", "croissant"]
    secret_word = random.sample(word_list, 1)[0] 
    print(secret_word)

    print(len(secret_word))
    letters = len(secret_word)

    display_word = list("_" * letters)
    print(display_word)
    first_guess = input("Guess a letter: ")
    # check to see if letter is in word
    indexes = []
    for idx, letter in enumerate(secret_word):
        if letter == first_guess:
            indexes.append(idx)
        print(indexes)
        print(idx, letter)
    for idx in indexes:
        display_word[idx] = first_guess
    print(f'display_word after modification {display_word}')
    # see if letter is in secret_word


    # validate the user input

main()