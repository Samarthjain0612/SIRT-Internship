from time import sleep
from pathlib import Path
import os

print("Loading", end="")
for i in range(3):
    sleep(1)
    print(".", end="")
print()
sleep(2)
print("\n--------------------FILE AND FOLDER SYSTEM MANAGEMENT INITIALIZED--------------------")

while True:
    try:
        print("\nChoose Suitable Option\n")
        print("1. Create Directory\n2. Read Directory\n3. Update Directory\n4. Delete Directory\n5. Create File\n6. Read File Data\n0. Exit App\n")
        n = int(input("Your Input: "))
        if n == 1:
            pathdir = input("\nEnter directory name/path: ")
            path = Path(pathdir)
            path.mkdir(exist_ok=False)
            print("-- FOLDER SUCCESSFULLY CREATED --")
        elif n == 2:
            path = Path('')
            for i, v in enumerate(path.rglob("*")):
                print(f"{i+1} . {v}")
            print("--  LIST OF FILES AND FOLDERS PRESENT --")
        elif n == 3:
            pathdir = input("Enter directory name/path to be renamed: ")
            path = Path(pathdir)
            path.rename(input("New Folder Name: "))
            print("-- FOLDER SUCCESSFULLY RENAMED --")
        elif n == 4:
            pathdir = input("Enter directory name/path to be deleted: ")
            path = Path(pathdir)
            filefolderlist = [i for i in path.rglob("*")]
            if len(filefolderlist) > 0:
                ask = input(
                    "Folder is not empty(You may loss data)\nDo you want to delete all files and folder?(Y/N)")
                if ask == 'Y' or ask == "y":
                    for i in filefolderlist:
                        if i.is_file():
                            os.remove(i)
                        else:
                            path1 = Path(i)
                            path1.rmdir()
                else:
                    continue
            path.rmdir()
            print("-- FOLDER REMOVED SUCCESSFULLY --")
        elif n == 5:
            path = Path('')
            for i, v in enumerate(path.rglob("*")):
                print(f"{i+1}. {v}")
            print("--  AVAILABLE FOLDERS TO CREATE FILE --")
            pathdir = input("Enter file name/path to be created: ")
            if Path(pathdir).exists():
                raise Exception("File Already Present!")
            with open(pathdir, 'w') as f:
                text = input("Enter file data(press enter to skip): ")
                f.write(text)
            print("-- FILE SUCCESSFULLY CREATED --")
        elif n == 6:
            path = Path('')
            for i, v in enumerate(path.rglob("*.*")):
                print(f"{i+1}. {v}")
            print("-- TOTAL FILES PRESENT --")
            pathdir = input("Enter file name/path to be read: ")
            with open(pathdir, 'r') as f:
                print("FETCHED DATA >> ", f.read())
                print("-- FILE DATA ENDS --")
            print("-- FILE SUCCESSFULLY READED --")
        elif n == 0:
            print("loading", end="")
            for i in range(3):
                sleep(1)
                print(".", end="")
            print()
            print("App closed!")
            break
        else:
            print("-- INVALID INPUT --")
    except Exception as err:
        print(err)
