n=int(input("Enter a number: "))
sum=0
for i in str(n):
    sum+=int(i)
if n%sum==0:
    print(n,"is a harshad number")
else:
    print(n,"is not a harshad number")