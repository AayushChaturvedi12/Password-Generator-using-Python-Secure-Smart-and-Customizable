import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x400")
        
        # Instructions
        self.label = tk.Label(root, text="Create strong and secure passwords to keep your account safe online.")
        self.label.pack(pady=10)
        
        # Generated Password display
        self.password_display = tk.Entry(root, width=30, font=("Arial", 14), state="readonly")
        self.password_display.pack(pady=10)
        
        # Generate Button
        self.generate_button = tk.Button(root, text="Generate", command=self.generate_password, bg="#4CAF50", fg="white", font=("Arial", 12))
        self.generate_button.pack(pady=10)
        
        # Copy Button
        self.copy_button = tk.Button(root, text="Copy", command=self.copy_password, bg="#4CAF50", fg="white", font=("Arial", 12))
        self.copy_button.pack(pady=5)
        
        # Password Options
        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.pack(pady=5)
        
        self.length_slider = tk.Scale(root, from_=6, to=20, orient="horizontal", length=200)
        self.length_slider.set(9)
        self.length_slider.pack(pady=5)
        
        # Character Options
        self.use_uppercase = tk.BooleanVar()
        self.use_lowercase = tk.BooleanVar(value=True)
        self.use_numbers = tk.BooleanVar()
        self.use_special = tk.BooleanVar(value=True)
        
        self.uppercase_checkbox = tk.Checkbutton(root, text="Include Uppercase", variable=self.use_uppercase)
        self.uppercase_checkbox.pack(pady=5)
        
        self.lowercase_checkbox = tk.Checkbutton(root, text="Include Lowercase", variable=self.use_lowercase)
        self.lowercase_checkbox.pack(pady=5)
        
        self.numbers_checkbox = tk.Checkbutton(root, text="Include Numbers", variable=self.use_numbers)
        self.numbers_checkbox.pack(pady=5)
        
        self.special_checkbox = tk.Checkbutton(root, text="Include Special Characters", variable=self.use_special)
        self.special_checkbox.pack(pady=5)
        
    def generate_password(self):
        length = self.length_slider.get()
        characters = ""
        characters += string.ascii_lowercase if self.use_lowercase.get() else ""
        characters += string.ascii_uppercase if self.use_uppercase.get() else ""
        characters += string.digits if self.use_numbers.get() else ""
        characters += string.punctuation if self.use_special.get() else ""
        
        if not characters:
            messagebox.showerror("Error", "At least one character option must be selected.")
            return
        
        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_display.config(state="normal")
        self.password_display.delete(0, tk.END)
        self.password_display.insert(0, password)
        self.password_display.config(state="readonly")
        
    def copy_password(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.password_display.get())
        self.root.update()
        messagebox.showinfo("Copied", "Password copied to clipboard")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
