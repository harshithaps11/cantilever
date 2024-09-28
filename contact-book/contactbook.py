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
    view_window.configure(bg='#fafafa')
    
    cursor.execute('SELECT * FROM contacts')
    contacts = cursor.fetchall()

    if contacts:
        for contact in contacts:
            contact_info = f"ID: {contact[0]} | Name: {contact[1]} | Phone: {contact[2]} | Email: {contact[3]}"
            tk.Label(view_window, text=contact_info, bg='#fafafa', font=('Arial', 12)).pack(pady=5)
    else:
        tk.Label(view_window, text="No contacts found.", bg='#fafafa', font=('Arial', 12)).pack(pady=5)

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
root.geometry("600x400")
root.configure(bg='#ffffff')

# Create Labels and Entry Fields with a modern look
tk.Label(root, text="Contact Book", font=('Helvetica', 24, 'bold'), bg='#2196f3', fg='white').pack(fill=tk.X, pady=10)

# Create a frame for the input fields
input_frame = tk.Frame(root, bg='#ffffff')
input_frame.pack(pady=10)

tk.Label(input_frame, text="Name", bg='#ffffff', font=('Arial', 12)).grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(input_frame, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(input_frame, text="Phone", bg='#ffffff', font=('Arial', 12)).grid(row=1, column=0, padx=10, pady=5)
phone_entry = tk.Entry(input_frame, width=30)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(input_frame, text="Email", bg='#ffffff', font=('Arial', 12)).grid(row=2, column=0, padx=10, pady=5)
email_entry = tk.Entry(input_frame, width=30)
email_entry.grid(row=2, column=1, padx=10, pady=5)

# Add Button
tk.Button(root, text="Add Contact", command=add_contact, bg='#4caf50', fg='white', font=('Arial', 14)).pack(pady=10)

# View Button
tk.Button(root, text="View Contacts", command=view_contacts, bg='#2196f3', fg='white', font=('Arial', 14)).pack(pady=10)

# Delete Section
delete_frame = tk.Frame(root, bg='#ffffff')
delete_frame.pack(pady=10)

tk.Label(delete_frame, text="Enter Contact ID to delete:", bg='#ffffff', font=('Arial', 12)).grid(row=0, column=0, padx=10)
contact_id_entry = tk.Entry(delete_frame, width=10)
contact_id_entry.grid(row=0, column=1, padx=10)

tk.Button(delete_frame, text="Delete Contact", command=delete_contact, bg='#f44336', fg='white', font=('Arial', 14)).grid(row=0, column=2, padx=10)

# Start the application
root.mainloop()

# Close the database connection when the app is closed
conn.close()

