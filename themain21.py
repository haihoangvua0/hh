import random

current_number = random.randint(0, 1)
current_player = ""

if current_number == 0:
    current_player = "human"
elif current_number == 1:
    current_player = "computer"

while current_number <= 21:

    if current_player == "human":
        player_choice = int(input("Your choice of number: "))
        while player_choice not in [1, 2, 3]:
            player_choice = int(input("Invalid choice. Choose 1, 2, or 3: "))
        current_number += player_choice
        print(f"Current number: {current_number}")
        if current_number >= 21:
            print("Computer wins!")
            break
        current_player = "computer"
            
    else:
        computer_choice = random.randint(1, 3)
        current_number += computer_choice
        print(f"Computer chose: {computer_choice}")
        print(f"Current number: {current_number}")
        if current_number >= 21:
            print("Human wins!")
            break
        current_player = "human"
