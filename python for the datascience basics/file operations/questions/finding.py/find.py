word = "learning"
with open(r"D:\python for the datascience basics\PYTHON\file operations\questions\replace java with pyhton\replace.txt","r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("found")
    else:
        print("not exist")
        