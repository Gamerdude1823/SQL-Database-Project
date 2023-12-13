import sqlite3
import tkinter as tk
from tkinter import ttk

# Create a SQLite database and a students table
conn = sqlite3.connect("student_database.db")
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        email TEXT
    )
''')
conn.commit()

class StudentManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")

        # Create labels and entry widgets
        self.label_name = ttk.Label(root, text="Name:")
        self.entry_name = ttk.Entry(root)

        self.label_email = ttk.Label(root, text="Email:")
        self.entry_email = ttk.Entry(root)

        self.label_age = ttk.Label(root, text="Age:")
        self.entry_age = ttk.Entry(root)

        # Create buttons
        self.button_add = ttk.Button(root, text="Add Student", command=self.add_student)
        self.button_view = ttk.Button(root, text="View Students", command=self.view_students)

        # Place widgets using grid layout
        self.label_name.grid(row=0, column=0, padx=10, pady=5)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        self.label_roll_number.grid(row=1, column=0, padx=10, pady=5)
        self.entry_roll_number.grid(row=1, column=1, padx=10, pady=5)

        self.label_age.grid(row=2, column=0, padx=10, pady=5)
        self.entry_age.grid(row=2, column=1, padx=10, pady=5)

        self.button_add.grid(row=3, column=0, columnspan=2, pady=10)
        self.button_view.grid(row=4, column=0, columnspan=2, pady=10)

    def add_student(self):
        name = self.entry_name.get()
        roll_number = self.entry_roll_number.get()
        age = self.entry_age.get()

        if name and roll_number and age:
            conn.execute("INSERT INTO students (name, roll_number, age) VALUES (?, ?, ?)", (name, roll_number, age))
            conn.commit()
            self.clear_entries()
            print("Student added successfully!")
        else:
            print("Please fill in all fields.")

    def view_students(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("View Students")

        tree = ttk.Treeview(view_window, columns=("ID", "Name", "Roll Number", "Age"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Name", text="Name")
        tree.heading("Roll Number", text="Roll Number")
        tree.heading("Age", text="Age")

        students = conn.execute("SELECT * FROM students").fetchall()

        for student in students:
            tree.insert("", "end", values=student)

        tree.pack(expand=True, fill="both")

    def clear_entries(self):
        self.entry_name.delete(0, "end")
        self.entry_roll_number.delete(0, "end")
        self.entry_age.delete(0, "end")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementApp(root)
    root.mainloop()

# Close the database connection when the application is closed
conn.close()
