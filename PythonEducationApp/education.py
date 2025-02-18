import tkinter as tk
from tkinter import messagebox

class EducationalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Educational App")
        self.questions = [
            ("What is the capital of France?", "Paris"),
            ("What is the capital of Germany?", "Berlin"),
            ("What is 2 + 2?", "4"),
            ("What is the capital of Spain?", "Madrid"),
            ("What is the capital of Italy?", "Rome"),
            ("What is 5 * 6?", "30"),
            ("What is the capital of Portugal?", "Lisbon")
        ]
        self.current_question = 0
        self.create_widgets()
        
    def create_widgets(self):
        self.question_label = tk.Label(self.root, text=self.questions[self.current_question][0])
        self.question_label.pack(pady=10)
        
        self.answer_entry = tk.Entry(self.root)
        self.answer_entry.pack(pady=10)
        
        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)
        
    def check_answer(self):    
        answer = self.answer_entry.get().strip().lower()
        correct_answer = self.questions[self.current_question][1]
        if answer == correct_answer:
            messagebox.showinfo("Correct", "Thats the right answer!")
            self.current_question += 1
            if self.current_question < len(self.questions):
                self.question_label.config(text=self.questions[self.current_question][0])
                self.answer_entry.delete(0, tk.END)
            else:
                messagebox.showinfo("End", "You have answered all questions!")
                self.root.quit()
        else:
            messagebox.showerror("Incorrect", "That is not the correct answer!")
            
if __name__ == "__main__":
    root = tk.Tk()
    app = EducationalApp(root)
    root.mainloop()                        
                
                
