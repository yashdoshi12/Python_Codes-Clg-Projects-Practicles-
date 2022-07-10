values = input("Input some comma seprated numbers : ")
list = values.split(",")
A = tuple(list)
print("Maximum element of tuple is",max(A), "and Minimum element of tuple is",min(A))