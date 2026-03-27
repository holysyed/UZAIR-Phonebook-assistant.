import json
import tkinter as tk
from tkinter import messagebox

# Load contacts
try:
    with open("contacts.json", "r") as file:
        contacts = json.load(file)
except:
    contacts = {}

# Functions
def add_contact():
    name = name_entry.get()
    number = number_entry.get()

    if name and number:
        contacts[name] = number

        with open("contacts.json", "w") as file:
            json.dump(contacts, file)

        messagebox.showinfo("Success", "Contact saved!")
        name_entry.delete(0, tk.END)
        number_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "Enter both fields Dumbo!")

def search_contact():
    name = name_entry.get()

    if name in contacts:
        messagebox.showinfo("Result", f"Number: {contacts[name]}")
    else:
        messagebox.showerror( "can not be found", "stored in your cerebal cortex?")

# GUI Setup
root = tk.Tk()
root.title("Uzair Phonebook Assistant")
root.geometry("550x450")

# Labels
tk.Label(root, text="Name").pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Number").pack(pady=5)
number_entry = tk.Entry(root)
number_entry.pack()

# Buttons
tk.Button(root, text="Add Contact", command=add_contact).pack(pady=10)
tk.Button(root, text="Search Contact", command=search_contact).pack(pady=5)

# Run app
root.mainloop()