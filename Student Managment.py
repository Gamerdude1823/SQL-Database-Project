import sqlite3
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

# Create a SQLite database and a students table
conn = sqlite3.connect("student_database.db")
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        gpa INTEGER,
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

        self.label_gpa = ttk.Label(root, text="Gpa:")
        self.entry_gpa = ttk.Entry(root)

        self.label_email = ttk.Label(root, text="Email:")
        self.entry_email = ttk.Entry(root)


        # Create buttons
        self.button_add = ttk.Button(root, text="Add Student", command=self.add_student)
        self.button_view = ttk.Button(root, text="View Students", command=self.view_students)
        self.button_remove = ttk.Button(root, text="Remove Student", command=self.remove_student)

        # Place widgets using grid layout
        self.label_name.grid(row=0, column=0, padx=10, pady=5)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        self.label_email.grid(row=1, column=0, padx=10, pady=5)
        self.entry_email.grid(row=1, column=1, padx=10, pady=5)

        self.label_gpa.grid(row=2, column=0, padx=10, pady=5)
        self.entry_gpa.grid(row=2, column=1, padx=10, pady=5)

        self.button_add.grid(row=3, column=0, columnspan=2, pady=10)
        self.button_view.grid(row=4, column=0, columnspan=2, pady=10)
        self.button_remove.grid(row=5, column=0, columnspan=2, pady=10)

# Adds a student to the database
    def add_student(self):
        name = self.entry_name.get()
        email = self.entry_email.get()
        gpa = self.entry_gpa.get()

        def error():
            messagebox.showerror('Data Error', 'Please fill out all fields!')
            return

        def success():
            messagebox.showinfo('Input Success', 'Student added to table!')
            return

        if name and email and gpa:
            conn.execute("INSERT INTO students (name, gpa, email) VALUES (?, ?, ?)", (name, gpa, email))
            conn.commit()
            self.clear_entries()
            success()
            return
        else:
            error()
            return

# Removes a student from the database
    def remove_student(self):
        remove_window = tk.Toplevel(self.root)
        remove_window.title("Remove Student")

        label_remove = ttk.Label(remove_window, text="Enter student ID to remove:")
        entry_remove = ttk.Entry(remove_window)
        button_confirm = ttk.Button(remove_window, text="Remove", command=lambda: self.confirm_remove(entry_remove.get()))
        
        label_remove.pack(pady=10)
        entry_remove.pack(pady=10)
        button_confirm.pack(pady=10)

    def confirm_remove(self, student_id):

        def remove_error():
            messagebox.showerror('Data Error', 'Please input valid student ID!')
            return

        def remove_success():
            messagebox.showinfo('Removal Successful', 'Student removed from database!')
            return         
     
        try:
            student_id = int(student_id)
            conn.execute("DELETE FROM students WHERE id=?", (student_id,))
            conn.commit()
            remove_success()
        except ValueError:
            remove_error()
        except Exception as e:
            messagebox.showerror(f"An error occurred: {str(e)}")

# allows a user to view students in database
    def view_students(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("View Students")

        tree = ttk.Treeview(view_window, columns=("ID", "Name", "Gpa" , "Email"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Name", text="Name")
        tree.heading("Email", text="Email")
        tree.heading("Gpa", text="Gpa")

        students = conn.execute("SELECT * FROM students").fetchall()

        for student in students:
            tree.insert("", "end", values=student)

        tree.pack(expand=True, fill="both")

    def clear_entries(self):
        self.entry_name.delete(0, "end")
        self.entry_email.delete(0, "end")
        self.entry_gpa.delete(0, "end")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementApp(root)
    root.mainloop()

# Close the database connection when the application is closed
conn.close()
