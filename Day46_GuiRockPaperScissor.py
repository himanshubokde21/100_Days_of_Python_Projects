import tkinter as tk
import random

class RockPaperScissors:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Rock Paper Scissors Game")

        self.player_score = 0
        self.computer_score = 0

        self.create_buttons()

        self.result_label = tk.Label(self.window, text="Choose your move!", font=("Arial", 15))
        self.result_label.pack(pady=10)

        self.message_label = tk.Label(self.window, text="", font=("Arial", 15))
        self.message_label.pack(pady=10)

        self.score_label = tk.Label(self.window, text=f"Player: {self.player_score} | Computer: {self.computer_score}")
        self.score_label.pack(pady=10)

    def create_buttons(self):
        frame = tk.Frame(self.window)
        frame.pack(padx=10, pady=10)

        choices = ['Rock ✊', 'Paper ✋', 'Scissors ✌️']

        for choice in choices:
            btn = tk.Button(frame, text=choice, command=lambda x=choice: self.play_game(x[:len(x)-2]))
            btn.pack(side=tk.LEFT, padx=10)

    def play_game(self, player_choice):
        computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
        result = self.determine_winner(player_choice, computer_choice)
        
        self.result_label.config(text=f"You chose {player_choice}, Computer chose {computer_choice}")
        
        if result == "Player":
            self.player_score += 1
        elif result == "Computer":
            self.computer_score += 1
        
        if result != "Tie":
            self.message_label.config(text=f"{result} Won!")
        self.score_label.config(text=f"Player: {self.player_score} | Computer: {self.computer_score}")

    def determine_winner(self, player, computer):
        if player == computer:
            self.message_label.config(text="It's a Tie!")
            return "Tie"
        elif (
            (player == 'Rock' and computer == 'Scissors') or
            (player == 'Paper' and computer == 'Rock') or
            (player == 'Scissors' and computer == 'Paper')
        ):          
            return "Player"
        else:
            return "Computer"

    def run(self):
        self.window.mainloop()

game = RockPaperScissors()
game.run()
