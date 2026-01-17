f = open(r"D:\python for the datascience basics\PYTHON\file operations\basic\sample.txt", "r")
data = f.read()

print(data)
print(type(data))

f.close()
