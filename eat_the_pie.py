import random


def validate_guess(guess, guessed_letters):
    if guess in guessed_letters:
        return (False, "You've already guessed this")

    if not guess.isalpha():
        return (False, "Letters only please")

    if len(guess) != 1:
        return (False, "One letter only please")

    return (True, "")


def generate_secret_word():
    word_list = [
        "recurse",
        "apple",
        "programming",
        "lists",
        "python",
        "games",
        "sustainable",
        "croissant",
    ]
    secret_word = random.sample(word_list, 1)[0].upper()

    return secret_word


def check_guess(secret_word, guess):
    # check to see if letter is in word
    indexes = []
    for idx, letter in enumerate(secret_word):
        if letter == guess:
            indexes.append(idx)

    return indexes


def display_word(secret_word):
    pass


def main():
    print("Welcome to Eat the Pie!")

    secret_word = generate_secret_word()
    print(secret_word)

    print(len(secret_word))
    letters = len(secret_word)
    pie_slices = 8

    display_word = list("_" * letters)
    print(display_word)

    guessed_letters = []
    while True:
        guess = input("Guess a letter: ")
        guess = guess.upper()

        validate_result = validate_guess(guess, guessed_letters)
        if validate_result[0] is False:
            print(validate_result[1])

        guessed_letters.append(guess)

        correct_indexes = check_guess(secret_word, guess)

        for idx in correct_indexes:
            display_word[idx] = guess
        print(f"display_word after modification {display_word}")

        # Next up:
        # Game end conditions
        # * You're outta pies
        # * You guessed the word (no underscores)
        # Display the pie slices
        if pie_slices == 0:
            print("You're outta pies buddy")
            break


if __name__ == "__main__":
    main()
