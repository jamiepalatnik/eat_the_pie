import random

def main():
    print("Welcome to Eat the Pie!")

    word_list = ["recurse", "apple", "programming", "lists", "python", "games", "sustainable", "croissant"]
    secret_word = random.sample(word_list, 1)[0] 
    print(secret_word)

    print(len(secret_word))
    letters = len(secret_word)

    print("_ " * letters)

main()