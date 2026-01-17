count = 0
# first open and read the file
with open(r"D:\python for the datascience basics\PYTHON\file operations\questions\count the even numbes in the file\even.txt","r") as f :
    data = f.read()
    # split the data or typecast it from string to the integes using split
    nums = data.split(",")

    #  usage of the loop to count the even numbers
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1
print(count) # print the count