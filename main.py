import customtkinter as ctk
import json

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Load contacts
try:
    with open("contacts.json", "r") as f:
        contacts = json.load(f)
except:
    contacts = {}

# Save contacts
def save_contacts():
    with open("contacts.json", "w") as f:
        json.dump(contacts, f, indent=4)

# Chat logic
def process_command(command):
    words = command.lower().split()

    if words[0] == "add" and len(words) >= 3:
        name = words[1]
        number = words[2]
        contacts[name] = number
        save_contacts()
        return f"✅ Added {name}"

    elif words[0] == "find" and len(words) >= 2:
        name = words[1]
        return contacts.get(name, "❌ Contact not found")

    elif words[0] == "delete" and len(words) >= 2:
        name = words[1]
        if name in contacts:
            del contacts[name]
            save_contacts()
            return f"🗑 Deleted {name}"
        return "❌ Contact not found"

    else:
        return "🤖 Try: add Ali 9876543210 / find Ali"

# Send message
def send_message():
    user_msg = entry.get()
    if not user_msg:
        return

    chatbox.insert("end", f"You: {user_msg}\n")
    response = process_command(user_msg)
    chatbox.insert("end", f"Uzair: {response}\n\n")
    entry.delete(0, "end")
    update_contact_list()

# Update sidebar
def update_contact_list():
    listbox.delete("0.0", "end")
    for name in contacts:
        listbox.insert("end", f"{name} : {contacts[name]}\n")

# App window
app = ctk.CTk()
app.title("Uzair Assistant")
app.geometry("700x450")

# Layout
frame = ctk.CTkFrame(app)
frame.pack(fill="both", expand=True, padx=10, pady=10)

# Sidebar
sidebar = ctk.CTkFrame(frame, width=200)
sidebar.pack(side="left", fill="y", padx=5, pady=5)

ctk.CTkLabel(sidebar, text="Contacts", font=("Arial", 16)).pack(pady=10)

listbox = ctk.CTkTextbox(sidebar, width=200)
listbox.pack(fill="both", expand=True, padx=5, pady=5)

# Chat area
chat_frame = ctk.CTkFrame(frame)
chat_frame.pack(side="right", fill="both", expand=True, padx=5, pady=5)

chatbox = ctk.CTkTextbox(chat_frame)
chatbox.pack(fill="both", expand=True, padx=5, pady=5)

entry = ctk.CTkEntry(chat_frame, placeholder_text="Type command...")
entry.pack(fill="x", padx=5, pady=5)

send_btn = ctk.CTkButton(chat_frame, text="Send", command=send_message)
send_btn.pack(pady=5)

update_contact_list()

app.mainloop()