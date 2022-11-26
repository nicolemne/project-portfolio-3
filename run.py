import random


def hangman_remaining_lives(lives):
    hangman_lives = [
        """
        ___________
        |/        |
        |         O
        |        /|\\
        |         |
        |        / \\
        |\\
        ========
        \n
        """,
        """
        ___________
        |/        |
        |         O
        |        /|\\
        |         |
        |        /
        |\\
        ========
        \n
        """,
        """
        __________
        |/        |
        |         O
        |        /|\\
        |         |
        |
        |\\
        ========
        \n
        """,
        """
        __________
        |/        |
        |         O
        |        /|
        |         |
        |
        |\\
        ========
        \n
        """,
        """
        __________
        |/        |
        |         O
        |         |
        |         |
        |
        |\\
        ========
        \n
        """,
        """
        __________
        |/        |
        |         O
        |
        |
        |
        |\\
        ========
        \n
        """,
        """
        __________
        |/
        |
        |
        |
        |
        |\\
        ========
        \n
        """,
        """
        __________
        |/
        |
        |
        |
        |
        |
        ========
        \n
        """,
        """
        |/
        |
        |
        |
        |
        |
        ========
        \n
        """,

        """
        |
        |
        |
        |
        |
        ========
        \n
        """,
        """
        """
        ]
    
    return hangman_lives[lives]


hangman_intro_image = [
        """
        ___________
        |/        |
        ||        O
        ||       /|\\    Press » 1  to start new game
        ||       / \\    Press » 2  for instructions
        ||              Press » 3  to select difficulty
        \n
        """,
        """
        """
]


def intro_title():
    """
    Function to display "Let's play Hangman" text when running the program
    """
    print("""
    █░░ █▀▀ ▀█▀ ▀ █▀   █▀█ █░░ ▄▀█ █▄█ 
    █▄▄ ██▄ ░█░ ░ ▄█   █▀▀ █▄▄ █▀█ ░█░ ▄ ▄ ▄
    """)
    print("""
    ██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
    ██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
    ███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
    ██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
    ██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
    ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
    """)


def start_options():
    """
    Function to display user choice to either
    start game, view instructions or select difficulty
    (User choice is displayed in the hangman_intro_image)
    """
    print(hangman_intro_image[0])
    
    start = False
    while not start:
        choice = input("\n ")
        if choice == "1":
            start = True
            difficulty = "default"
            return difficulty

        elif choice == "2":
            start = True
            hangman_instructions()
        
        elif choice == "3":
            start = True
            game_difficulty()

        else:
            print(f" You selected {choice}. "
                  "Please select 1, 2 or 3 to continue ♥")


def game_difficulty():
    """
    Function to select difficulty
    """
    print("\n")
    print("Please select a difficulty\n")
    print("Press E for Easy")
    print("Press N for Normal")
    print("Press H for Hard")
    
    difficulty = False
    while not difficulty:
        options = input("\n ").upper()
        if options == "E":
            difficulty = True
            difficulty_lives = 10
            return difficulty_lives
        elif options == "N":
            difficulty = True
            difficulty_lives = 7
            return difficulty_lives
        elif options == "H":
            difficulty = True
            difficulty_lives = 5
            return difficulty_lives
        else:
            print("\n Please choose E, N or H to select your difficulty")


def get_word():
    """
    Gets random word form cities.txt
    """
    word = random.choice(open("cities.txt", "r").read().split('\n'))
    return word.upper()


def play_game(word, difficulty_lives):
    secret_word = "_" * len(word)
    game_over = False
    guesses = []
    lives = difficulty_lives
    print("Good luck!")
    print(f"Remaining Lives: {lives}\n")
    print("Your city to guess: " + " ".join(secret_word) + "\n")
    print("\n")

    while not game_over and lives > 0:
        input_guess = input("Please guess a letter: \n").upper()
        try:
            if len(input_guess) > 1:
                raise ValueError(
                    f"\nYou can only guess one letter at the time. "
                    f"You guessed: {len(input_guess)}."
                )
            elif not input_guess.isalpha():
                raise ValueError(
                    f"Only letters allowed."
                    f"You guessed: {len(input_guess)}."
                )
            elif len(input_guess) == 1 and input_guess.isalpha():
                if input_guess in guesses: 
                    raise ValueError(
                        f"You have already guessed {input_guess}."
                        )
                elif input_guess not in word:
                    print(f"Sorry, wrong guess... {input_guess}"
                          " is not in the word")
                    print("You lost a life. Better luck next time!")
                    guesses.append(input_guess)
                    lives -= 1
                else:
                    print(f"You found a letter! {input_guess} is correct. GG!")
                    guesses.append(input_guess)
                    guessed_word_list = list(secret_word)
                    indices = [i for i, letter in enumerate(word)
                               if letter == input_guess]
                    for index in indices:
                        guessed_word_list[index] = input_guess
                        secret_word = "".join(guessed_word_list)
                    if "_" not in secret_word:
                        game_over = True
        
        except ValueError as input_error:
            print(f"{input_error}.\nPlease try again.\n")
            continue

        print(hangman_remaining_lives(lives))

        if lives > 0:
            print(f"Remaining Lives: {lives}\n")
            print(" Your city to guess: " + " ".join(secret_word) + "\n")
            print(" Your guesses: " + ", ".join(sorted(guesses)) + "\n")

    if game_over:
        print(f"Congrats, you found the secret word: {word}!")
    
    else:
        print("Oh shoot! You're out of lives.")
        print("Game over.\n\n")
        print(f"The correct word was: {word}")


def hangman_instructions():
    """
    Function to display help instructions for game rules.
    Starts the game when user enters S
    """
    print("\n")
    print("A name of a city will be hidden behind blank spaces.\n"
          "You must find the correct city by guessing each letter.\n"
          "Correct guesses will reveal a letter in the name.\nWrong guesses "
          "will reduce a life.\n\nHope you have fun!\n")

    main_menu = input("Press enter to return to main"
                      " menu\n")
    print("\n")
    main()


def main():
    """
    Start the application
    """
    intro_title()
    difficulty = start_options()
    if difficulty == "default":
        difficulty_lives = 7
    else:
        difficulty_lives = game_difficulty()
    hangman_word = get_word()
    play_game(hangman_word, difficulty_lives)


main()
