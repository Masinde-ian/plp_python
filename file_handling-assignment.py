# file_handling_assignment.py

def create_file():
    # Task 1: Create a new text file named "my_file.txt" in write mode ('w')
    try:
        with open("my_file.txt", "w") as file:
            # Write at least three lines of text to the file
            file.write("Hello, this is line 1.\n")
            file.write("12345 is a number.\n")
            file.write("Python is awesome!\n")
        print("File 'my_file.txt' created successfully.")
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")

def read_and_display():
    # Task 2: Read the contents of "my_file.txt" and display them on the console
    try:
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("\nContents of 'my_file.txt':\n")
            print(content)
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")

def append_to_file():
    # Task 3: Open "my_file.txt" in append mode ('a') and append three additional lines
    try:
        with open("my_file.txt", "a") as file:
            file.write("\nAppending a new line.\n")
            file.write("More text goes here.\n")
            file.write("Final line added.\n")
        print("\nFile 'my_file.txt' updated successfully.")
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")

if __name__ == "__main__":
    create_file()
    read_and_display()
    append_to_file()
