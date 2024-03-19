import psycopg2 #import the psycopg2 module(README)
import json

with open('databaseInfo.json', 'r') as f: #make sure the json file matches
    config = json.load(f)

DB_NAME = config['database']['DB_NAME']
DB_USER = config['database']['DB_USER']
DB_PASS = config['database']['DB_PASS']
DB_HOST = config['database']['DB_HOST']
DB_PORT = config['database']['DB_PORT']


def get_connection():
    return psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)

def getAllStudents():
    with get_connection() as conn:
        with conn.cursor() as curs:
            curs.execute("SELECT * FROM students") #QUery to select all students
            student_records = curs.fetchall()
            for student in student_records:
                print(student)

def addStudent(first_name, last_name, email, enrollment_date):
    with get_connection() as conn:
        with conn.cursor() as curs:
            curs.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                         (first_name, last_name, email, enrollment_date)) # Query to insert a new student
            conn.commit()
            print("Student added successfully")

def updateStudentEmail(student_id, new_email):
    with get_connection() as conn:
        with conn.cursor() as curs:
            curs.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id)) # Query to update email
            conn.commit()
            print("Email updated successfully")

def deleteStudent(student_id):
    with get_connection() as conn:
        with conn.cursor() as curs:
            curs.execute("DELETE FROM students WHERE student_id = %s", (student_id,)) # Query to delete a student
            conn.commit()
            print("Student deleted successfully")

# If you want to test the functions

#getAllStudents()
#addStudent('Alice', 'Johnson', 'alice.johnson@example.com', '2024-01-01')
#updateStudentEmail(4, 'new.email@example.com')       
#deleteStudent(4           
#getAllStudents()

# Easiest way to test all funcitons

def main_menu():
    while True:
        print("\nWelcome to the Student Management System")
        print("1. List all students")
        print("2. Add a new student")
        print("3. Update a student's email")
        print("4. Delete a student")
        print("5. Exit")
        
        choice = input("Enter the number of your choice: ")
        
        if choice == '1':
            getAllStudents()
        elif choice == '2':
            first_name = input("Enter student's first name: ")
            last_name = input("Enter student's last name: ")
            email = input("Enter student's email: ")
            enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")
            addStudent(first_name, last_name, email, enrollment_date)
        elif choice == '3':
            student_id = input("Enter student's ID to update email: ")
            new_email = input("Enter student's new email: ")
            updateStudentEmail(student_id, new_email)
        elif choice == '4':
            student_id = input("Enter student's ID to delete: ")
            deleteStudent(student_id)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
