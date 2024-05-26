import random

def user_choice():
    while True:
        n = input("Enter your choice (rock, paper, scissor): ")
        n = n.lower()
        if n in ["rock", "paper", "scissor"]:
            return n
        else:
            print("Invalid input! Please enter rock, paper, or scissor.")

def machine_choice():
    return random.choice(["rock", "paper", "scissor"])

def winner(n, c):
    if n == c:
        return "Tie"
    elif (n == "rock" and c == "scissor") or (n == "paper" and c == "rock") or (n == "scissor" and c == "paper"):
        return "You win!"
    else:
        return "I win!"

def play_game():
    uc = 0
    cp = 0
    while True:
        n = user_choice()
        c = machine_choice()
        print("You chose:", n)
        print("I chose:", c)
        win = winner(n, c)
        if win == "You win!":
            uc = uc+1
        elif win == "I win!":
            cp =cp+1
        print(f"win: {win}")
        print(f"Your Score: {uc} | My Score: {cp}")
        again = input("Do you want to play again? Type yes or no: ")
        if again.lower() != "yes":
            print("Thanks for playing the game!")
            break

play_game()
