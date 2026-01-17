f = open(r"D:\python for the datascience basics\PYTHON\file operations\write\write.txt","w")

f.write("hello world of the python") 
# w is used to write or to overwrite on the text

f = open(r"D:\python for the datascience basics\PYTHON\file operations\write\write.txt","a")
f.write("\nhello to the world of the reactjs")
# a is used to append the write to the end of the file
f.close()