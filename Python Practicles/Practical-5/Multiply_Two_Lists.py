A=list(map(int,input("Enter Elements for Set A.: ").split()))
B=list(map(int,input("Enter Elements for Set A.: ").split()))

products = [a * b for a, b in zip(A, B)]

print(products)