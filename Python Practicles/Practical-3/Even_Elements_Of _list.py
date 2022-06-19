l=eval(input("Enter a list: "))
length=len(l)
print("List elements at even position are: ")
for i in range(0,length,2):
    print(l[i],end=' ')