import sqlite3
import time

#connects to database
connection = sqlite3.connect('students.db')
cursor = connection.cursor()

#checks for datbase and creates it if not detected
cursor.execute("CREATE TABLE IF NOT EXISTS students (name TEXT gpa TEXT email TEXT)") 

def get_name(cursor):
    cursor.exceute("SELECT name FROM students")
    results = cursor.fetchall()
    if len(results) == 0:
        print("No Students in Database")
        return None
    for i in range(len(results)):
        print(f"{i+1}- {results[i][0]}")
    choice = 0 
    while choice < 1 or choice > len(results):
        choice =int(input("Name ID: "))
    return results [choice-1][0]


choice = None
# User menu 
while choice != "5":
    time.sleep(1)
    print("______WELCOME TO THE STUDNET MANAGMENT DATABASE ______")
    print("1) Show list of Students Enrolled ")
    print("2) Update Student Information ")
    print("3) Add New Student")
    print("4) Remove Student")
    print("5) Quit")
    choice = input("> ")
    print()
    if choice == "1":
        time.sleep(1)
        # Shows list of students
        cursor.execute("SELECT * FROM students ORDER BY name DESC")
        print("{:>10}  {:>10}  {:>10}". format ("Name", "GPA", "Email"))
        for record in cursor.fetchall():
            print("{:>10}  {:>10}  {:>10}" .format(record[0], record[1], record[2]))
     
    elif choice == "2":
        time.sleep(1)
        # Update student info
        
        try:
            name = input ("Name: ")
            gpa = float(input ("GPA: "))
            email = input("Email: ")
            values = (name, gpa, email)
            cursor.execute("UPDATE employees SET pay = ? WHERE name = ?", values)
            connection.commit()
            if cursor.rowcount == 0:
                print("Invalid Name!")
        except ValueError:
            print("Invalid Input!")

    elif choice == "3":
        time.sleep(1)
        # Add new student
        try:
            name = input ("Name: ")
            gpa = float(input ("GPA: "))
            email = input("Email: ")
            values = (name, gpa, email)
            cursor.execute("INSERT INTO students VALUES (?,?,?)", values)
            connection.commit()
        except ValueError:
            print("Invalid Input")

    elif choice == "4":
        time.sleep(1)
        # remove student
        name = get_name(cursor)
        if name == None:
            continue
        values = (name)
        cursor.execute("DELETE FROM students WHERE name = ?", values)
        connection.commit()
    print()

connection.close()

