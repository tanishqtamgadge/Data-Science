import os

if os.path.exists(r"D:\python for the datascience basics\PYTHON\file operations\delete\delete.txt"):
    os.remove(r"D:\python for the datascience basics\PYTHON\file operations\delete\delete.txt")
else:
    print("File does not exist")
