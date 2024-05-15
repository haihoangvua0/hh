import random
curren_number = random.randint(0, 1)
curren_player = ""


while True:
    if curren_number == 0:
        curren_player = "human"
    if curren_number == 1:
        curren_player = "computer"
    while curren_number <= 21:
        if curren_player == "human":
            player_choice = int(input("Your choice of number: "))
            while player_choice in [1, 2, 3]:
                print(player_choice)
                if player_choice != [1, 2, 3]:
                    curren_number += player_choice
                curren_player = "computer"
                
        else:
            computer_choice = random.randint(1, 3)
            print(computer_choice)
            curren_number += computer_choice
            if curren_number <= 21:
                print(curren_number)
                print("Human win")
            else:
                curren_player = 'human'
    break
