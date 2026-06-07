from pathlib import Path

def createfile():
    try:
        name = input("Please tell your file name: ")
        path = Path(name)
        if not path.exists():
            with open(path, "w") as fs:
                data = input("What do you want to write: ")
                fs.write(data)
            print("File created successfully")
        else:
            print("File already exists")
    except Exception as err:
        print("An error occurred:", err)

def readfile():
    try:
        name = input("Please tell your file name: ")
        path = Path(name)
        if path.exists():
            with open(path, "r") as fs:
                content = fs.read()
            print("\nFile Content:")
            print(content)
        else:
            print("Error: No such file exists")
    except Exception as err:
        print("An error occurred:", err)

def updatefile():
    try:
        name = input("Please tell your file name: ")
        path = Path(name)
        if path.exists():
            print("\nOperations:")
            print("1. Rename the file")
            print("2. Append content")
            print("3. Overwrite the file")
            choice = int(input("Enter your option: "))
            if choice == 1:
                newname = input("Enter new file name: ")
                new_path = Path(newname)
                if not new_path.exists():
                    path.rename(new_path)
                    print("File renamed successfully")
                else:
                    print("A file with that name already exists")
            elif choice == 2:
                with open(path, "a") as fs:
                    data = input("What do you want to append: ")
                    fs.write("\n" + data)
                print("Content appended successfully")
            elif choice == 3:
                with open(path, "w") as fs:
                    data = input("What do you want to overwrite with: ")
                    fs.write(data)
                print("File overwritten successfully")
            else:
                print("Invalid option")
        else:
            print("Error: No such file exists")
    except Exception as err:
        print("An error occurred:", err)

def deletefile():
    try:
        name = input("Please tell your file name: ")
        path = Path(name)
        if path.exists():
            path.unlink()
            print("File deleted successfully")
        else:
            print("Error: No such file exists")
    except Exception as err:
        print("An error occurred:", err)

print("\n===== FILE MANAGER =====")
print("1. Create a file")
print("2. Read a file")
print("3. Update a file")
print("4. Delete a file")

a = int(input("\nEnter your choice: "))

if a == 1:
    createfile()
elif a == 2:
    readfile()
elif a == 3:
    updatefile()
elif a == 4:
    deletefile()
else:
    print("Invalid choice")
