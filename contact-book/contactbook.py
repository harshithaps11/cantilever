import tkinter as tk
from tkinter import messagebox
import sqlite3

# Create or connect to a database
conn = sqlite3.connect('contacts.db')
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS contacts
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                phone TEXT,
                email TEXT)''')

# Function to add a contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()

    if name and phone and email:
        cursor.execute('INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)', (name, phone, email))
        conn.commit()
        messagebox.showinfo("Success", "Contact added!")
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "All fields are required!")

# Function to view all contacts
def view_contacts():
    view_window = tk.Toplevel()
    view_window.title("All Contacts")
    
    cursor.execute('SELECT * FROM contacts')
    contacts = cursor.fetchall()

    if contacts:
        for contact in contacts:
            contact_info = f"ID: {contact[0]} | Name: {contact[1]} | Phone: {contact[2]} | Email: {contact[3]}"
            tk.Label(view_window, text=contact_info).pack()
    else:
        tk.Label(view_window, text="No contacts found.").pack()

# Function to delete a contact
def delete_contact():
    contact_id = contact_id_entry.get()
    if contact_id:
        cursor.execute('DELETE FROM contacts WHERE id = ?', (contact_id,))
        conn.commit()
        messagebox.showinfo("Success", "Contact deleted!")
        contact_id_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Contact ID is required!")

# GUI Setup
root = tk.Tk()
root.title("Contact Book")

# Create Labels and Entry Fields
tk.Label(root, text="Name").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Phone").grid(row=1, column=0)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1)

tk.Label(root, text="Email").grid(row=2, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1)

# Add Button
tk.Button(root, text="Add Contact", command=add_contact).grid(row=3, column=0, columnspan=2)

# View Button
tk.Button(root, text="View Contacts", command=view_contacts).grid(row=4, column=0, columnspan=2)

# Delete Section
tk.Label(root, text="Enter Contact ID to delete:").grid(row=5, column=0)
contact_id_entry = tk.Entry(root)
contact_id_entry.grid(row=5, column=1)

tk.Button(root, text="Delete Contact", command=delete_contact).grid(row=6, column=0, columnspan=2)

# Start the application
root.mainloop()

# Close the database connection when the app is closed
conn.close()