
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image
import pytesseract
from PyPDF2 import PdfReader
from transformers import BertForQuestionAnswering, AutoTokenizer, pipeline

# Additional import for themed tkinter
from ttkthemes import ThemedStyle

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Initialize the pipeline outside the functions
nlp = pipeline('question-answering', model=BertForQuestionAnswering.from_pretrained('deepset/bert-base-cased-squad2'),
              tokenizer=AutoTokenizer.from_pretrained('deepset/bert-base-cased-squad2'))

def process_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
        return text

def process_image(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

def open_file_dialog():
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("All files", "*.*")])
    if file_path:
        # Set the global variable here
        global selected_file_path
        selected_file_path = file_path
        # Display the content of the selected file
        display_file_content(selected_file_path)
        return True
    return False

def ask_question():
    question = entry.get()
    global selected_file_path
    if selected_file_path:
        if selected_file_path.lower().endswith('.pdf'):
            text = process_pdf(selected_file_path)
        elif selected_file_path.lower().endswith(('.jpg', '.png', '.jpeg')):
            text = process_image(selected_file_path)

        answer = nlp({
            'question': question,
            'context': text
        })

        result_text.set(answer['answer'])

def display_file_content(file_path):
    # Clear existing content
    file_content_text.delete("1.0", tk.END)
    
    # Display the content of the file
    if file_path.lower().endswith('.pdf'):
        text = process_pdf(file_path)
    elif file_path.lower().endswith(('.jpg', '.png', '.jpeg')):
        text = process_image(file_path)
    
    file_content_text.insert(tk.END, text)

# Create the main window with themed style
window = tk.Tk()
window.title("PDF Insight Assistant")
window.iconbitmap("favicon.ico")

# Apply a themed style to the window
style = ThemedStyle(window)
style.set_theme("arc")  # You can choose different themes: "aquativo", "arc", "radiance", etc.

# Set the window size and background color
window.geometry("800x600")  # Adjust the size as needed
window.configure(bg='#0CECF7')  # Background color

# Create and configure themed widgets
question_label = ttk.Label(window, text="Enter your question:",  background='#0CF7CC', font=('Segoe UI Light', 15, 'bold'))
question_label.pack(pady=10)

entry = ttk.Entry(window, width=40)
entry.pack(pady=10)

browse_button = ttk.Button(window, text="Browse File", command=open_file_dialog)
browse_button.pack(pady=10)

# Text widget to display the content of the selected file
file_content_text = tk.Text(window, wrap="word", height=10, width=60)
file_content_text.pack(pady=10)

ask_button = ttk.Button(window, text="Ask Question", command=ask_question)
ask_button.pack(pady=10)

result_label = ttk.Label(window, text="Answer:",  background='#0CF7CC', font=('Segoe UI Light', 15, 'bold'))
result_label.pack(pady=10)

result_text = tk.StringVar()
result_entry = ttk.Entry(window, textvariable=result_text, state='readonly', width=40)
result_entry.pack(pady=10)

# Start the GUI event loop
window.mainloop()







