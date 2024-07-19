import tkinter as tk
from tkinter import messagebox

def add_item():
    item = entry.get()
    if item:
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def remove_item():
    try:
        selected_index = listbox.curselection()[0]
        listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to remove.")

def mark_done():
    try:
        selected_index = listbox.curselection()[0]
        item = listbox.get(selected_index)
        if not item.startswith("[DONE]"):
            listbox.delete(selected_index)
            listbox.insert(selected_index, f"[DONE] {item}")
        else:
            messagebox.showinfo("Info", "Task already marked as done.")
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to mark as done.")


root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(pady=10)
custom_font=("Brownie Stencil",12)
entry = tk.Entry(frame, width=50)
entry.pack(side=tk.LEFT, padx=10)

add_button = tk.Button(frame, text="Add", command=add_item,font=custom_font)
add_button.pack(side=tk.LEFT)

remove_button = tk.Button(root, text="Remove", command=remove_item,font=custom_font)
remove_button.pack(pady=5)

done_button = tk.Button(root, text="Done", command=mark_done,font=custom_font)
done_button.pack(pady=5)

listbox = tk.Listbox(root, width=50, height=10,font=custom_font)
listbox.pack()


root.mainloop()
