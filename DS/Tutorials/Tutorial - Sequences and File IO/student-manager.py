import os

def display_menu():
    """
    Display the menu options.
    """
    print("\nStudent Management System Menu:")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. View All Students")
    print("5. Exit")


def add_student(students):
    """
    Add a new student record.
    """
    name = input("Enter student name: ")
    id = input("Enter student ID: ")
    students[id] = name
    print("Student added successfully!")


def update_student(students):
    """
    Update an existing student record.
    """
    id = input("Enter student ID to update: ")
    if id in students:
        name = input("Enter updated student name: ")
        students[id] = name
        print("Student updated successfully!")
    else:
        print("Student ID not found!")


def delete_student(students):
    """
    Delete an existing student record.
    """
    id = input("Enter student ID to delete: ")
    if id in students:
        del students[id]
        print("Student deleted successfully!")
    else:
        print("Student ID not found!")


def view_all_students(students):
    """
    View all student records.
    """
    if students:
        print("\nAll Students:")
        for id, name in students.items():
            print(f"ID: {id}, Name: {name}")
    else:
        print("No student records found!")


def load_students(filename):
    """
    Load student records from a file.
    """
    students = {}
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                id, name = line.strip().split(",")
                students[id] = name
    return students


def save_students(filename, students):
    """
    Save student records to a file.
    """
    with open(filename, "w") as file:
        for id, name in students.items():
            file.write(f"{id},{name}\n")


def main():
    filename = "student_records.txt"
    students = load_students(filename)

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            update_student(students)
        elif choice == "3":
            delete_student(students)
        elif choice == "4":
            view_all_students(students)
        elif choice == "5":
            save_students(filename, students)
            print("Student records saved. Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
