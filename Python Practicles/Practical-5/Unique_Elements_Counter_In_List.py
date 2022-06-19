A=list(map(int,input("Please entere elements of lists.: ").split()))
B=[]
for i in A:
    if A.count(i)==1:
        B.append(i)
if len(B)==0:
    print("No unique element found")
else:
    print("Unique elements are.: ",B)