import random

# Track scores across multiple rounds
player_score = 0
computer_score = 0

# Main game loop
while True:
    player = 0
    computer = 0
    
    print('''
          
===================
Rock Paper Scissors
===================
1) ✊
2) ✋
3) ✌️


''')

    player_choice = int(input('Choose your weapon (or 0 to quit): '))
    if player_choice == 0:
        break
    
    if player_choice == 1:
        player = 'rock'
    elif player_choice == 2:
        player = 'paper'
    elif player_choice == 3:
        player = 'scissors'
    else:
        print('Invalid choice. Please choose 1, 2, or 3.')
        continue

    computer_choice = random.randint(1, 3)
    if computer_choice == 1:
        computer = 'rock'
    elif computer_choice == 2:
        computer = 'paper'
    elif computer_choice == 3:
        computer = 'scissors'

    print(f'You chose {player}.')
    print(f'The computer chose {computer}.')

    if player == computer:
        print("It's a tie!")
    elif (player == 'rock' and computer == 'scissors') or (player == 'paper' and computer == 'rock') or (player == 'scissors' and computer == 'paper'):
        print("You win!")
        player_score += 1
    else:
        print("You lose!")
        computer_score += 1
        
    print(f"Score: You {player_score} - Computer {computer_score}")
    print("\nEnter 0 to quit or choose your next weapon.\n")
# End of game

print("\nThanks for playing!")
print(f"Final score: You {player_score} - Computer {computer_score}")
# This is a Rock-Paper-Scissors game where the player can play multiple rounds against the computer.
# The game tracks scores and allows players to quit at any time.