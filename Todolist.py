import tkinter as tk
from tkinter import messagebox
 
def add_item():
    item = entry.get()
    if item:
        listbox.insert(tk.END, f"🌸 {item}")
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty Entry", "Please enter a task.")
 
def remove_item():
    selected_index = listbox.curselection()
    if selected_index:
        listbox.delete(selected_index)
    else:
        messagebox.showinfo("No Selection", "Please select a task to remove.")
 
root = tk.Tk()
root.title("'*•.¸♡ ♡¸.•* WELCOME TO THE TO DO LIST  APP'*•.¸♡ ♡¸.•")
 
listbox = tk.Listbox(root, selectbackground="pink")
listbox.pack(padx=10, pady=10)
 
entry = tk.Entry(root, width=30)
entry.pack(pady=10)
 
add_button = tk.Button(root, text="Add Task", command=add_item)
add_button.pack()
 
remove_button = tk.Button(root, text="Remove Task", command=remove_item)
remove_button.pack()
 
root.mainloop()
 
