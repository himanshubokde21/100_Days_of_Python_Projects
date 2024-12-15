import random
import time
def RockPaperScissors():
    choice = {1: 'rock', 2: 'paper', 3: 'scissor'}
    while True: 
        print('''
Enter your Choice: 
    1. enter "paper" for Paper.
    2. enter "rock" for Rock.
    3. enter "scissor" for Scissors.
    ''')
        user = input("Enter your Choice: ") 
        while user != 'rock' and user != 'paper' and user != 'scissor':
            print("Invalid Choice")
            user = input("Enter Valid Choice: ")
        print(f'User Choice is: {user}')
        print("Now it's computer's Turn...")
        ComChoice = random.randint(1, 3)
        computer = choice[ComChoice]
        time.sleep(2)
        print(f"Computer Choice is: {computer}")
        print(f"{user} vs {computer}")
        if user == computer:
            print('<== It\'s a Tie! ==>')
        elif user == 'rock':
            if computer == 'scissor':
                print('<== User Wins! ==>')
            else:
                print('<== Computer Wins! ==>')
        elif user == 'paper':
            if computer == 'scissor':
                print('<== Computer Wins! ==>')
            else:
                print('<== User Wins! ==>')
        else:
            if computer == 'paper':
                print('<== User Wins! ==>')
            else:
                print('<== Computer Wins! ==>')
        play = input("Do you want to Play agian? (Y/N): ")
        while play != 'Y' and play != 'y' and play != 'N' and play != 'n':
            print("wrong Response")
            play = input("Enter again (Y/N): ")
        if play == 'N' or play == 'n':
            print("Thanks for playing!")
            break

print('''
Winning rules of the game Rock-Paper-Scissors are:
    Rock vs Paper -> Paper Wins.
    Rock vs Scissors -> Rock Wins.
    Paper vs Scissors -> Scissors Wins. ''')
RockPaperScissors()