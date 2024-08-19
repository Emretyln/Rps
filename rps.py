import random

# Introduction to game and gameplay

def rock_paper_scissors_EMRE_YAVUZ():
    print("Welcome to Rock Paper Scissors Game!")
    print("Rules:"
          "Rock crushes Scissors."
          "Scissors cuts Paper."
          "Paper covers Rock.")
    print("Who wins first two rounds will be the game winner.")
    print("If you want to quit press q.\n")

    choice = ["rock", "paper", "scissors"]

    while True:
        your_score = 0
        opponent_score = 0

        # Main loop of the game
        while your_score < 2 and opponent_score < 2:
            you = input("rock, paper, scissors? ").lower()

            if you == 'q':
                print("Quitting game!")
                return

            if you not in choice:
                print("Invalid choice. Please try again.")
                continue

            opponent_choice = random.choice(choice)
            print(f"Opponent choice: {opponent_choice}")

            if you == opponent_choice:
                print("Draw!")
            elif (you == "rock" and opponent_choice == "scissors") or \
                    (you == "paper" and opponent_choice == "rock") or \
                    (you == "scissors" and opponent_choice == "paper"):

                # Win round = +1 point
                print("You WIN!")
                your_score += 1
            else:
                print("Opponent WINS!")
                opponent_score += 1

            print(f"Score: You {your_score} - Opponent {opponent_score}")

        # Picking game winner
        if your_score == 2:
            print("Congrats, You Win the game!")
        else:
            print("Sorry, Opponent Wins the game!")

        # Play again
        play_again = input("Do you want to play again? (yes/no) ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

        opponent_play_again = random.choice(["yes", "no"])
        print(f"Opponent: {opponent_play_again}")
        if opponent_play_again != "yes":
            print("Opponent quit. Thanks for playing!")
            break

rock_paper_scissors_EMRE_YAVUZ()
