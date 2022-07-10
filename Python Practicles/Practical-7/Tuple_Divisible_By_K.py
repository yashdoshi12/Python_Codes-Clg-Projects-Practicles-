my_list = [(50, 30, 23), (34, 102, 22), (24, 246 , 23), (270, 450, 810)]

K = 45

my_result = [sub for sub in my_list if all(ele % K == 0 for ele in sub)]

print("Elements divisible by K are : " + str(my_result))