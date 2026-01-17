def check_for_word():
    word = "learning"
    with open(r"D:\python for the datascience basics\PYTHON\file operations\questions\replace java with pyhton\replace.txt","r") as f:
        data = f.read()
        if(word in data):
            print("found")
        else:
            print("not found")

def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open(r"D:\python for the datascience basics\PYTHON\file operations\questions\replace java with pyhton\replace.txt","r") as f:
        while data :
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1

check_for_line()