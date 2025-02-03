from tkinter import *
from tkinter import ttk, messagebox
import googletrans
import textblob

# Create the main application window
root = Tk()
root.title("Google Translator")
root.geometry("1080x400")
img_icon = PhotoImage(file="data/google.png")
root.iconphoto(False, img_icon)

# Function to update displayed languages
def lbl_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000, lbl_change)

# Function to perform translation
def translate():
    global lang
    try:
        text_ = text1.get(1.0, END).strip()  # Strip whitespace from input
        c3 = combo2.get()  # Target language
        
        if not text_:
            messagebox.showwarning("Input Error", "Please enter text to translate.")
            return
        
        if c3 == "SELECT LANGUAGE":
            messagebox.showwarning("Language Error", "Please select a target language.")
            return

        words = textblob.TextBlob(text_)
        lan = words.detect_language()  # Detect the language of the input text

        # Find the target language code
        for i, j in lang.items():
            if j == c3:
                lan_ = i
                break
        
        # Perform translation
        translated_text = words.translate(from_lang=lan, to=str(lan_))
        
        # Update output text area with translated text
        text2.delete(1.0, END)
        text2.insert(END, translated_text)
    
    except googletrans.TranslatorError as te:
        messagebox.showerror("Translation Error", f"Translation failed: {str(te)}")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

# Load arrow image for UI
arrow_img = PhotoImage(file="data/arrow.png")
img_lbl = Label(root, image=arrow_img, width=150)
img_lbl.place(x=460, y=50)

# Initialize language options
lang = googletrans.LANGUAGES
langV = list(lang.values())
lang_keys = list(lang.keys())

# Create source language combobox
combo1 = ttk.Combobox(root, values=langV, font="Roboto 14", state="readonly")
combo1.place(x=110, y=20)
combo1.set("ENGLISH")

# Create label for source language display
label1 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="white", width=18, bd=5, relief="groove")
label1.place(x=10, y=50)

# Create frame and text area for input
f = Frame(root, bg="black", bd=5)
f.place(x=10, y=118, width=440, height=210)

text1 = Text(f, font="Roboto 20", bg="white", relief="groove", wrap='word')
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side='right', fill="y")
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# Create target language combobox
combo2 = ttk.Combobox(root, values=langV, font="Roboto 14", state="readonly")
combo2.place(x=730, y=20)
combo2.set("SELECT LANGUAGE")

# Create label for target language display
label2 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="white", width=18, bd=5, relief="groove")
label2.place(x=620, y=50)

# Create frame and text area for output
f1 = Frame(root, bg="black", bd=5)
f1.place(x=620, y=118, width=440, height=210)

text2 = Text(f1, font="Roboto 20", bg="white", relief="groove", wrap='word')
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side='right', fill="y")
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

# Create translate button
trans_btn = Button(root, text="Translate", font="Roboto 15 bold italic",
                   activebackground="purple", cursor="hand2",
                   bd=5, bg="red", fg="white", command=translate)
trans_btn.place(x=480, y=250)

# Start updating language labels
lbl_change()

# Configure main window background color and start the main loop
root.configure(bg="white")
root.mainloop()
