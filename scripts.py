# Lab3/script.py

def write_file_with_name():
    name = input("Enter your name: ")
    with open("output.txt", "w") as file:
        file.write(f"My name is: {name}")

# Test the function
write_file_with_name()
