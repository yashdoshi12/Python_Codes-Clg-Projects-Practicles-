x=input("Please enter the word.: ")
test_str = input("Please enter the string.: ")

count = 0
 
for i in test_str:
    if i == x:
        count = count + 1
print (" The count is : " + str(count))