import random


# oyun tanıtımı ve oynanış

def rock_paper_scissors():
    choice = ["rock", "paper", "scissors"]
    your_score = 0
    opponent_score = 0

    # Oyunun ana döngüsü

    while your_score < 2 and opponent_score < 2:
        you = input("rock, paper, scissors? ").lower()
        opponent_choice = random.choice(choice)
        print(f"Opponent choice: {opponent_choice}")

        if you == opponent_choice:
            print("Draw!")
        elif (you == "rock" and opponent_choice == "scissors") or \
                (you == "paper" and opponent_choice == "rock") or \
                (you == "scissors" and opponent_choice == "paper"):

            # tur döngüsü, kazanan +1 puan alıyor

            print("You WIN!")
            your_score += 1
        else:
            print("Opponent WIN!")
            opponent_score += 1

        print(f"Skor: You {your_score} - Opponent {opponent_score}")

    # oyun galibini belirleme

    if your_score == 2:
        print("Congrats, You Win the game!")
    else:
        print("Sorry, Opponent Win the game!")

    # tekrar oyna

    play_again = input("Do you want to play again? (yes/no) ").lower()
    if play_again == "yes":
        rock_paper_scissors()


rock_paper_scissors()