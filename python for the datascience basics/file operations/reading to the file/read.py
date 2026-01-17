f = open(r"D:\python for the datascience basics\PYTHON\file operations\reading to the file\read.txt","r")
# da = f.read() reads the entire file
# data = f.read(5) reads the 5 indexes onlu from 0 to 5

data = f.read()
print(data)
# if the file is already readed we cant read it again
line1 = f.readline()
# print(data)
line2 = f.readline()
print(line1)
print(line2)
f.close()