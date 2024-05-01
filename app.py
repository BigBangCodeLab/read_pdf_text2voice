import tkinter as tk
from tkinter import filedialog
import PyPDF2
import pyttsx3

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text

def play_text():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        text = read_pdf(file_path)

        # Initialize the text-to-speech engine
        engine = pyttsx3.init()

       # Set properties
        engine.setProperty('rate', 180)  # Speed of speech

        # Set Indian English voice (Change 'en-in' to 'hi' for Hindi)
        engine.setProperty('voice', 'english+f4')  # Use 'f4' for female voice
        
        # Convert text to speech
        engine.say(text)

        # Wait for the speech to finish
        engine.runAndWait()

root = tk.Tk()
root.title("PDF Reader")

# Header Label
header_label = tk.Label(root, text="PDF Reader", font=("Arial", 18, "bold"))
header_label.pack(pady=10)

# Button to select PDF and play
play_button = tk.Button(root, text="Select PDF and Play", command=play_text, font=("Arial", 12))
play_button.pack(pady=10)

# Instruction Label
instruction_label = tk.Label(root, text="Click the button below to select a PDF file and play its content.", wraplength=300)
instruction_label.pack()

root.mainloop()
