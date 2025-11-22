nums = (1,4,9,16,25,36,47,64,81,100)
idx = 0
x = int(input("Enter the value of x:"))

while idx < len(nums):
    if(nums[idx]==x):
       print("Found at index :" , idx)
    idx += 1
else:
    print("Not in the list")
