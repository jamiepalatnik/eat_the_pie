import random
from term_piechart import Pie


def validate_guess(guess, guessed_letters):
    if guess in guessed_letters:
        return (False, "You've already guessed this")

    if not guess.isalpha():
        return (False, "Letters only please")

    if len(guess) != 1:
        return (False, "One letter only please")

    return (True, "")


def generate_secret_word(difficulty_level):
    match difficulty_level:
        case "1":
            word_list_filename = "easy-words.txt"
        case "2":
            word_list_filename = "normal-words.txt"
        case "3":
            word_list_filename = "hard-words.txt"

    word_list = []
    with open(word_list_filename, "r") as fh:
        for line in fh:
            word_list.append(line.strip())

    secret_word = random.sample(word_list, 1)[0].upper()

    return secret_word


def check_guess(secret_word, guess):
    # check to see if letter is in word
    indexes = []
    for idx, letter in enumerate(secret_word):
        if letter == guess:
            indexes.append(idx)

    return indexes


def display_pie_chart(starting_pie_slices, pie_slices_remaining):
    # starting_pie_slices 8
    # pie_slices 3
    pie_slices = [
        {
            "name": "Pie Slices Remaining",
            "value": pie_slices_remaining,
            "color": "#CA8606",
        },
        {
            "name": "Eaten",
            "value": (starting_pie_slices - pie_slices_remaining),
            "color": "#ffffff",
        },
    ]

    pie = Pie(
        pie_slices,
        radius=10,
        autocolor_pastel_factor=0.7,
        legend={"line": 0, "format": "{label} {name:<8} {percent:>5.2f}% [{value}]"},
    )
    print("")
    print(pie.render())


def main():
    print("Welcome to Eat the Pie!")
    print("")

    while True:
        print("Choose your difficulty")
        print("1. a-la-mode [easy]")
        print("2. apple [normal]")
        print("3. humble [hard]")
        difficulty_level = input("1 2 or 3?: ")

        if difficulty_level == "":
            difficulty_level = "2"

        if difficulty_level in ["1", "2", "3"]:
            break

    match difficulty_level:
        case "1":
            starting_pie_slices = pie_slices = 12
        case "2":
            starting_pie_slices = pie_slices = 8
        case "3":
            starting_pie_slices = pie_slices = 6

    display_pie_chart(starting_pie_slices, pie_slices)

    secret_word = generate_secret_word(difficulty_level)
    # print(f"Secret word: {secret_word}")

    letters = len(secret_word)

    display_word = list("_" * letters)
    print(" ".join(display_word))

    guessed_letters = []

    while True:
        guess = input("Guess a letter: ")
        guess = guess.upper()

        validate_result = validate_guess(guess, guessed_letters)
        if validate_result[0] is False:
            print(validate_result[1])
            continue

        # Add letter to guessed letters
        guessed_letters.append(guess)

        correct_indexes = check_guess(secret_word, guess)

        # If guess is not correct, lose one piece of pie
        if len(correct_indexes) == 0 and pie_slices > 2:
            pie_slices = pie_slices - 1
            print(f"There are {pie_slices} pieces of pie remaining.")
        elif len(correct_indexes) == 0 and pie_slices == 2: 
            pie_slices = pie_slices - 1
            print(f"There is {pie_slices} piece of pie remaining.")
        elif len(correct_indexes) == 0 and pie_slices == 1:
            pie_slices = pie_slices - 1
        else:
            # If guess is correct
            for idx in correct_indexes:
                display_word[idx] = guess
            print(f"There are {pie_slices} pieces of pie remaining.")
        display_pie_chart(starting_pie_slices, pie_slices)
        print(" ".join(display_word))
        print("Guessed letters: ", " ".join(guessed_letters))

        # Next up:
        # Game end conditions
        # * You're outta pies
        # * You guessed the word (no underscores)
        if display_word == list(secret_word):
            print("You guessed the word!")
            break

        # Display the pie slices
        if pie_slices == 0:
            print(f"You're outta pies buddy. The secret word was: {secret_word}")
            break


if __name__ == "__main__":
    main()
