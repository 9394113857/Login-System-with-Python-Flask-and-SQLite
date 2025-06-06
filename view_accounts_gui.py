import sqlite3
import tkinter as tk
from tkinter import ttk

# ✅ Database and Table Info
DB_PATH = r'instance\pythonlogin.db'
TABLE_NAME = 'account'

# ✅ Connect to the SQLite database
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# ✅ Fetch all records from the 'account' table
try:
    cursor.execute(f"SELECT id, username, email FROM {TABLE_NAME}")
    accounts = cursor.fetchall()
except sqlite3.OperationalError as e:
    print("Database Error:", e)
    accounts = []

conn.close()

# ✅ Create the main GUI window
root = tk.Tk()
# root.title(f"Viewing Database: {DB_PATH} | Table: {TABLE_NAME}")
root.title(f"Viewing Database: Table: {TABLE_NAME}")


# Set fixed size and center the window on screen
window_width = 650
window_height = 450
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# ✅ Title label
title_label = tk.Label(
    root,
    text=f"Showing: {DB_PATH} → Table: {TABLE_NAME}",
    font=("Segoe UI", 12, "bold"),
    fg="blue"
)
title_label.pack(pady=(10, 5))

# ✅ Treeview style and configuration
style = ttk.Style()
style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))
style.configure("Treeview", font=("Segoe UI", 10), rowheight=30)

tree = ttk.Treeview(root, columns=("ID", "Username", "Email"), show='headings')
tree.heading("ID", text="ID")
tree.heading("Username", text="Username")
tree.heading("Email", text="Email")

tree.column("ID", anchor='center', width=50)
tree.column("Username", anchor='center', width=200)
tree.column("Email", anchor='center', width=350)

# ✅ Insert data into the table
for account in accounts:
    tree.insert('', tk.END, values=account)

tree.pack(expand=True, fill='both', padx=20, pady=10)

# ✅ Exit Button
exit_btn = tk.Button(root, text="Exit", command=root.destroy, font=("Segoe UI", 10), width=12)
exit_btn.pack(pady=10)

# ✅ Start the GUI loop
root.mainloop()
