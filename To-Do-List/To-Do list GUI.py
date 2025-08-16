import tkinter as tk
from tkinter import messagebox
import json
import os

# File to store tasks
TASKS_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks():
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f)

# Add a new task
def add_task():
    task_text = entry.get().strip()
    if task_text:
        tasks.append({"task": task_text, "done": False})
        update_listbox()
        save_tasks()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Oops!", "Please enter a task before adding.")

# Mark selected task as done
def mark_done():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]["done"] = not tasks[index]["done"]
        update_listbox()
        save_tasks()
    else:
        messagebox.showinfo("Hey!", "Please select a task to mark.")

# Delete selected task
def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        deleted_task = tasks.pop(index)
        update_listbox()
        save_tasks()
        messagebox.showinfo("Deleted", f"Removed: {deleted_task['task']}")
    else:
        messagebox.showwarning("Oops!", "Please select a task to delete.")

# Update listbox display
def update_listbox():
    listbox.delete(0, tk.END)
    for t in tasks:
        status = "✔" if t["done"] else "✘"
        listbox.insert(tk.END, f"{t['task']}  [{status}]")

# -------- Main GUI --------
root = tk.Tk()
root.title("📝 My Friendly To-Do List")
root.geometry("400x500")
root.config(bg="#f5f5f5")

tasks = load_tasks()

# Title
title_label = tk.Label(root, text="My To-Do List", font=("Arial", 20, "bold"), bg="#f5f5f5")
title_label.pack(pady=10)

# Entry box
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10, padx=20, fill=tk.X)

# Buttons
btn_frame = tk.Frame(root, bg="#f5f5f5")
btn_frame.pack(pady=5)

add_btn = tk.Button(btn_frame, text="➕ Add", width=8, command=add_task, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
add_btn.grid(row=0, column=0, padx=5)

done_btn = tk.Button(btn_frame, text="✔ Done", width=8, command=mark_done, bg="#2196F3", fg="white", font=("Arial", 12, "bold"))
done_btn.grid(row=0, column=1, padx=5)

delete_btn = tk.Button(btn_frame, text="🗑 Delete", width=8, command=delete_task, bg="#F44336", fg="white", font=("Arial", 12, "bold"))
delete_btn.grid(row=0, column=2, padx=5)

# Task Listbox
listbox = tk.Listbox(root, font=("Arial", 14), height=15, selectbackground="#ffcc80")
listbox.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

# Scrollbar
scrollbar = tk.Scrollbar(listbox)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

update_listbox()

root.mainloop()
