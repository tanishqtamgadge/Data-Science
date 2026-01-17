with open(r"D:\python for the datascience basics\PYTHON\file operations\with sytax\demo.txt","r") as f:
    data = f.read()
    print(data)
# first the data is readed in the terminal
with open(r"D:\python for the datascience basics\PYTHON\file operations\with sytax\demo.txt","w") as f:
    f.write("hello")

# then the data is overwrite using the w mode
