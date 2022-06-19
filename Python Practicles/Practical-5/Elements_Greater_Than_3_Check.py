A=list(map(int,input("Enter Elements for Set A.: ").split()))
B=list(map(int,input("Enter Elements for Set B.: ").split()))
print("Difference Between two lists.: ",list(set(A)-set(B))+list(set(B)-set(A)))