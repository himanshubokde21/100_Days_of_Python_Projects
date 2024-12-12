import tkinter as tk
from tkinter import ttk
from textblob import TextBlob

def check_spelling():
    """Checks spelling for the entered text and corrects errors."""
    input_text = enter_text.get("1.0", tk.END).strip()
    if not input_text:
        result_label.config(text="Please enter a sentence!")
        return
    try:
        blob = TextBlob(input_text)
        corrected_text = blob.correct()
        if input_text.lower() == str(corrected_text).lower():
            result_label.config(text="The sentence is correct!", fg="green")
        else:
            highlighted_text = highlight_corrections(input_text, corrected_text)
            result_label.config(text=f"Corrected Sentence:\n{highlighted_text}", fg="blue", justify="left")
    except Exception as e:
        result_label.config(text="An error occurred while checking spelling.", fg="red")

def highlight_corrections(original, corrected):
    """Highlights corrected words in the sentence."""
    original_words = original.split()
    corrected_words = str(corrected).split()
    highlighted = []
    for o_word, c_word in zip(original_words, corrected_words):
        if o_word.lower() != c_word.lower():
            highlighted.append(f"[{c_word}]")  # Bracket corrected words for visibility
        else:
            highlighted.append(c_word)
    return " ".join(highlighted)

def clear_text():
    """Clears the input and output fields."""
    enter_text.delete("1.0", tk.END)
    result_label.config(text="")
    word_count_label.config(text="Word Count: 0")

def update_word_count(event=None):
    """Updates the word count label."""
    text = enter_text.get("1.0", tk.END).strip()
    word_count = len(text.split())
    word_count_label.config(text=f"Word Count: {word_count}")

# Initialize main window
root = tk.Tk()
root.title("Spelling Checker")
root.geometry("800x500")
root.config(bg="#e8f1f5")

# Main heading
heading = tk.Label(root, text="Spelling Checker", font=("Trebuchet MS", 35, "bold"), bg="#e8f1f5", fg="#1c3b57")
heading.pack(pady=10)

# Input Frame
input_frame = tk.Frame(root, bg="#e8f1f5")
input_frame.pack(pady=20)

input_label = tk.Label(input_frame, text="Enter Sentence:", font=("Arial", 14), bg="#e8f1f5", fg="#1c3b57")
input_label.grid(row=0, column=0, sticky="w", padx=5)

enter_text = tk.Text(input_frame, height=5, width=60, font=("Arial", 14), wrap="word", relief="solid", bd=2)
enter_text.grid(row=1, column=0, padx=10)
enter_text.bind("<KeyRelease>", update_word_count)

word_count_label = tk.Label(input_frame, text="Word Count: 0", font=("Arial", 12), bg="#e8f1f5", fg="#1c3b57")
word_count_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)

# Buttons
button_frame = tk.Frame(root, bg="#e8f1f5")
button_frame.pack(pady=10)

check_button = ttk.Button(button_frame, text="Check Spelling", command=check_spelling)
check_button.grid(row=0, column=0, padx=10)

clear_button = ttk.Button(button_frame, text="Clear", command=clear_text)
clear_button.grid(row=0, column=1, padx=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 16), bg="#e8f1f5", fg="#1c3b57", wraplength=750, justify="center")
result_label.pack(pady=20)

# Run the application
root.mainloop()
