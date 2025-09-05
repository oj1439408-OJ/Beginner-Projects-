import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Invalid Length", "Password length must be at least 4 characters.")
            return

        characters = ""
        if var_upper.get():
            characters += string.ascii_uppercase
        if var_lower.get():
            characters += string.ascii_lowercase
        if var_digits.get():
            characters += string.digits
        if var_symbols.get():
            characters += string.punctuation

        if not characters:
            messagebox.showwarning("No Selection", "Please select at least one character type.")
            return

        password = "".join(random.choice(characters) for _ in range(length))
        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length.")

# Function to copy password
def copy_password():
    password = result_entry.get()
    if password:
        window.clipboard_clear()
        window.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Empty", "No password to copy.")

# Function to clear/reset everything
def clear_all():
    length_entry.delete(0, tk.END)
    result_entry.delete(0, tk.END)
    var_upper.set(True)
    var_lower.set(True)
    var_digits.set(True)
    var_symbols.set(False)

# Main window
window = tk.Tk()
window.title("🔐 Password Generator")
window.geometry("400x450")
window.configure(bg="#2c3e50")

# Title Label
title_label = tk.Label(window, text="Password Generator", font=("Arial", 18, "bold"), fg="white", bg="#2c3e50")
title_label.pack(pady=10)

# Length input
length_frame = tk.Frame(window, bg="#2c3e50")
length_frame.pack(pady=10)
length_label = tk.Label(length_frame, text="Password Length:", font=("Arial", 12), fg="white", bg="#2c3e50")
length_label.pack(side=tk.LEFT, padx=5)
length_entry = tk.Entry(length_frame, font=("Arial", 12), width=5, justify="center")
length_entry.pack(side=tk.LEFT, padx=5)

# Checkboxes for complexity
var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=False)

options_frame = tk.Frame(window, bg="#2c3e50")
options_frame.pack(pady=10)

tk.Checkbutton(options_frame, text="Uppercase (A-Z)", variable=var_upper, bg="#2c3e50", fg="white", selectcolor="#34495e").pack(anchor="w")
tk.Checkbutton(options_frame, text="Lowercase (a-z)", variable=var_lower, bg="#2c3e50", fg="white", selectcolor="#34495e").pack(anchor="w")
tk.Checkbutton(options_frame, text="Digits (0-9)", variable=var_digits, bg="#2c3e50", fg="white", selectcolor="#34495e").pack(anchor="w")
tk.Checkbutton(options_frame, text="Symbols (!@#$...)", variable=var_symbols, bg="#2c3e50", fg="white", selectcolor="#34495e").pack(anchor="w")

# Generate button
generate_btn = tk.Button(window, text="Generate Password", font=("Arial", 12, "bold"), bg="#27ae60", fg="white", activebackground="#2ecc71", command=generate_password)
generate_btn.pack(pady=10)

# Result entry
result_entry = tk.Entry(window, font=("Arial", 14), width=30, justify="center")
result_entry.pack(pady=10)

# Buttons frame
btn_frame = tk.Frame(window, bg="#2c3e50")
btn_frame.pack(pady=10)

copy_btn = tk.Button(btn_frame, text="Copy to Clipboard", font=("Arial", 12), bg="#2980b9", fg="white", activebackground="#3498db", command=copy_password)
copy_btn.grid(row=0, column=0, padx=5)

clear_btn = tk.Button(btn_frame, text="Clear", font=("Arial", 12), bg="#c0392b", fg="white", activebackground="#e74c3c", command=clear_all)
clear_btn.grid(row=0, column=1, padx=5)

# Run the app
window.mainloop()
