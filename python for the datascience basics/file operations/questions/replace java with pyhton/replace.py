f = open(r"D:\python for the datascience basics\PYTHON\file operations\questions\replace java with pyhton\replace.txt","r")

data = f.read()

new_data = data.replace("Java","Python")
print(new_data)

f = open(r"D:\python for the datascience basics\PYTHON\file operations\questions\replace java with pyhton\replace.txt","w")
f.write(new_data)
f.close()
