import json
import tkinter as tk

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

        status_label.config(text="✅ Contact saved!", fg="#00ffcc")
        name_entry.delete(0, tk.END)
        number_entry.delete(0, tk.END)
    else:
        status_label.config(text="⚠️ Fill all fields!", fg="orange")


def search_contact():
    name = name_entry.get()

    if name in contacts:
        status_label.config(text=f"📞 {contacts[name]}", fg="#00ffcc")
    else:
        status_label.config(text="❌ Stored in your cerebal cortox?", fg="red")


# Main Window
root = tk.Tk()
root.title("Uzair Assistant")
root.geometry("400x350")
root.config(bg="#0f172a")  # dark background

# Title
tk.Label(root, text="UZair Phonebook", 
         font=("Helvetica", 18, "bold"), 
         bg="#0f172a", fg="#38bdf8").pack(pady=15)

# Frame (card style)
frame = tk.Frame(root, bg="#1e293b", padx=20, pady=20)
frame.pack(pady=10)

# Name
tk.Label(frame, text="Name", bg="#1e293b", fg="white").grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(frame, width=25)
name_entry.grid(row=1, column=0, pady=5)

# Number
tk.Label(frame, text="Number", bg="#1e293b", fg="white").grid(row=2, column=0, sticky="w")
number_entry = tk.Entry(frame, width=25)
number_entry.grid(row=3, column=0, pady=5)

# Buttons
tk.Button(frame, text="Add Contact", bg="#22c55e", fg="white",
          width=20, command=add_contact).grid(row=4, column=0, pady=10)

tk.Button(frame, text="Search Contact", bg="#3b82f6", fg="white",
          width=20, command=search_contact).grid(row=5, column=0)

# Status label (UX improvement)
status_label = tk.Label(root, text="", bg="#0f172a", fg="white", font=("Arial", 10))
status_label.pack(pady=10)

# Run app
root.mainloop()