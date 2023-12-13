# Overview

For this project I wrote a Student Managment service utilizing the Python language.

I have a line of code that, when the code is run, it checks for the existance of a database called students located within the exisiting folder and of it is not found then a new one is created wih the proper headings for the data that the program deals with. Such as the name of each studnet, their gpa and their email address. When the code is started a simple interface appears and ask for imput. The user can then slesct if they want to either:
Update an existing students information
Add a new student
Remove studnet 
or quit the program
the user is asked returned to the interface after each process is completed unless the quit option is selected. It is a simple program but utilizes a local SQL database where data can be queryed for and displayed to a user. 

I wanted to see how a SQL database can be intigrated so that I could potentially use it for other projects in the future. I currently do not have any ideas for the future use of an SQL database but it is good to understand for the future!

{Provide a link to your YouTube demonstration. It should be a 4-5 minute demo of the software running, a walkthrough of the code, and a view of how created the Relational Database.}

[Software Demo Video](http://youtube.link.goes.here)

# Relational Database

I am using the SQL service SQLite3 which is a database service engine. This is a local database created in VScode along side your project. This database funtions like any other. The data can be added or removed as well as organized into columns or rows so that specific can be queryed for the user. The data is also able to be displayed to the user however the programmer decides. SQLite utlizes the Schema Table for it database which is a description of the data that is contained within the program be it table or otherwise.

# Development Environment

I utilized the IDE VScode and the programing language Python. I also used the SQL program SQLite which allows for the creation of local databases and managment of those databases and the data they contain. I also utilized the time library so to add a little style for myself and others that I found appealing. I used the sleep function to create pauses within the code to give it the appeal of a loading within the program. 

# Useful Websites

{Make a list of websites that you found helpful in this project}

- [SQLite](https://www.sqlite.org/index.html)
- [W3Schools Sqlite tutorial](https://www.w3schools.blog/sqlite-tutorial)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}

- Creating an actual unser interface that looks cleaner and more appealing than a IDE terminal 
- Add more options so that more can be done with this database. maybe allow for diffrent databases to be created
- Clean up the code and ultilize more features of Python