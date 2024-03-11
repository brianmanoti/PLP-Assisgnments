def create_file():
  """ function that creates a file """
    try:
        with open("my_file.txt", "w") as file:
            file.write("Hello, this is line 1.\n")
            file.write("12345\n")
            file.write("Another line, line 3.\n")
        print("File created successfully!")
    except (PermissionError, FileNotFoundError) as e:
        print(f"Error creating file: {e}")
    finally:
        print("File creation process completed.")


def read_file():
  """ function to read the contents of a file """
    try:
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("Content of my_file.txt:")
            print(content)
    except (PermissionError, FileNotFoundError) as e:
        print(f"Error reading file: {e}")
    finally:
        print("File reading process completed.")


def append_to_file():
  """ function to append/add contents to a file """
    try:
        with open("my_file.txt", "a") as file:
            file.write("This line is appended.\n")
            file.write("54321\n")
            file.write("Last line, appended line.\n")
        print("Appended to file successfully!")
    except (PermissionError, FileNotFoundError) as e:
        print(f"Error appending to file: {e}")
    finally:
        print("File appending process completed.")


if __name__ == "__main__":
    create_file()
    read_file()
    append_to_file()
    read_file()
