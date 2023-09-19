import sqlite3

connection = sqlite3.connect()
cursor = connection.cursor()

cursor.execute("CREATE TABEL IF NOT EXISTS students (name TEXT, GPA)")

def get_name(cursor):
    cursor.exceute("SELECT name FROM students")
    results = cursor.fetchall()
    if len(results) == 0:
        print("No Students on Database")
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
    print("______WELCOME TO THE STUDNET MANAGMENT DATABASE ______")
    print("1) Show list of Students Enrolled ")
    print("2) Update Student Information ")
    print("3) Add New Student")
    print("4) Remove Student")
    print("5) Quit")
    choice = input("> ")
    print()
    if choice == "1":
        # Shows list of students
        cursor.execute("SELECT * FROM students ORDER BY name DESC")
        print("{:>10}  {:>10}  {:>10}". format ("Name", "GPA", "Email"))
        for record in cursor.fetchall():
            print("{:>10}  {:>10}  {:>10}" .format(record[0], record[1], record[2]))
     
    elif choice == "2":
        # Update student info
        pass

    elif choice == "3":
        # Add new student
        try:
            name = input ("Name: ")
            gpa = float(input ("GPA: "))
            email = input("Email: ")
            values = (name, gpa, email)
            cursor.execute("INSERT INTO students VALUES (?,?,?)", values)
            connection.commit()
        except:
            print("Invalid Input")

    elif choice == "4":
        # remove student
        name = get_name(cursor)
        if name == None:
            continue
        values = (name)
        cursor.execute("DELETE FROM students WHERE name = ?", values)
        connection.commit()
    print()

connection.close()
