import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)
def get_user_choice():
    user_input = input("Please enter your choice, rock, paper or scissors: ")
    return user_input

def health(user_choice,player_choice,com_hp,player_hp):
    if user_choice == computer_choice:
        player_hp -=1
    if user_choice == "rock" and computer_choice == "scissors":
        com_hp -=1
    if user_choice == "paper" and computer_choice == "rock":
        com_hp -=1
    
    if user_choice ==  "scissors" and computer_choice == "paper":
        com_hp -=1
    else:
        player_hp -=1
    return (player_hp,com_hp)
        
        
    
def play_game():
    player_hp = 5
    com_hp = 5

    while player_hp > 0 and com_hp > 0:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print("You chose...", user_choice)
        print("Opponent chose...", computer_choice)
        player_hp, com_hp = health(player_hp, com_hp, user_choice, computer_choice)
    
    if player_hp <1:
        print ("You Died!")
    if com_hp <1:
        print ("You win")

play_game()
