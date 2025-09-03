import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation!")
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="Result: ")
    operation_var.set('+')

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x300")

# Labels and entries for numbers
tk.Label(root, text="First Number:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Second Number:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack()

# Operation selection
operation_var = tk.StringVar(value='+')
tk.Label(root, text="Operation:").pack(pady=5)
operations_frame = tk.Frame(root)
operations_frame.pack()

def set_operation(op):
    operation_var.set(op)

tk.Button(operations_frame, text="+", command=lambda: set_operation('+')).pack(side=tk.LEFT, padx=5)
tk.Button(operations_frame, text="-", command=lambda: set_operation('-')).pack(side=tk.LEFT, padx=5)
tk.Button(operations_frame, text="*", command=lambda: set_operation('*')).pack(side=tk.LEFT, padx=5)
tk.Button(operations_frame, text="/", command=lambda: set_operation('/')).pack(side=tk.LEFT, padx=5)

# Calculate button
tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

# Clear button
tk.Button(root, text="Clear", command=clear).pack(pady=5)

# Result label
result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=5)

# Start the GUI loop
root.mainloop()
