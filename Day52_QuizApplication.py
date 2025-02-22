import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")

        self.questions = [
            {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
            {"question": "What is the largest planet in our solar system?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Jupiter"},
            {"question": "What is the chemical symbol for water?", "options": ["H2O", "O2", "CO2", "HO"], "answer": "H2O"}
        ]
        self.current_question_index = 0
        self.score = 0

        self.question_label = tk.Label(root, text=self.questions[self.current_question_index]["question"])
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for option in self.questions[self.current_question_index]["options"]:
            button = tk.Button(root, text=option, command=lambda opt=option: self.check_answer(opt))
            button.pack(pady=5)
            self.option_buttons.append(button)

        self.score_label = tk.Label(root, text=f"Score: {self.score}")
        self.score_label.pack(pady=20)

    def check_answer(self, selected_option):
        correct_answer = self.questions[self.current_question_index]["answer"]
        if selected_option == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct!", "Well done!")
        else:
            messagebox.showerror("Wrong!", f"The correct answer was {correct_answer}.")

        self.update_score()
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.update_question()
        else:
            self.show_results()

    def update_question(self):
        question_data = self.questions[self.current_question_index]
        self.question_label.config(text=question_data["question"])
        for i, option in enumerate(question_data["options"]):
            self.option_buttons[i].config(text=option)

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")

    def show_results(self):
        messagebox.showinfo("Quiz Finished", f"Your score is {self.score} out of {len(self.questions)}")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
