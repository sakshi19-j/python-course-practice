import random
user_input = int(input("Type 0 for rock, 1 for paper or 2 for scissors.\n"))
choice= ["rock", "paper", "scissors"]
computer_choice = random.choice(choice)
print(f"you chose {choice[user_input]}")
print(f"computer chose {computer_choice}")

if choice[user_input] == computer_choice:
    print("it's a draw")
elif choice[user_input] == "scissors" and computer_choice == "rock":
    print("you win")
elif choice[user_input] == "paper" and computer_choice == "rock":
    print("you win")
elif choice[user_input] == "scissors" and computer_choice == "paper":
    print("you win")
else:
    print("you lose")
