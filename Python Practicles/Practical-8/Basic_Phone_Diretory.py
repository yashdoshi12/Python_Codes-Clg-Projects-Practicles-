print("\nWecome to Mangaon's biggest Phone data space.\n")
print("Here you can perform basic operations on the data.\n")
print("-------------------------------------------------------------------------------------\n")

phone_list = {"Mr.A":9786756453, "Mr.B":8067946587, "Mr.C":9089780878, "Mr.D": 7898561209, "Mr.E":9809896767}

def home_page():
    print(''' Choose any one of the below options,\n
            1. To display updated phone directory.
            2. To change the number of a person.
            3. To change name of person associated to a number.
            4. To Find a exixting phone number.
            5. To delete a person from list.
               Type exit to exit\n''')

def check_list():
    print("This is the Updated list of Phone numbers\n")
    print(phone_list)

def find():
    print("Here you can find the number associated to a name.\n")
    name = input("Please enter a valid name: ")
    if name in phone_list:
        print("\nThe phone number of", name, "is", phone_list[name])
    else:
        print("You have entered the wrong name!")

def replace_number():
    print("Here you can replace number associated to a name.\n")
    replace_name = input("Please enter the name of person: ")
    replaced_number = input("\nPlease enter the updated number: ")
    phone_list[replace_name] = replaced_number

def replace_name():
    print("Here you can replace name associated to a number.\n")
    find_name = input("Please enter the name you wish to change: ")
    update_name = input("\nPlease enter the updated name:")
    phone_list[find_name] = update_name

def delete_name():
    print("Here you can delete a name and number of a person.\n")
    del_name = input("Please enter the name of person: ")
    if delete_name in phone_list:
        phone_list.pop(delete_name)
    else:
        print("Wrong name entered.")

home_page()
while True:
        key=str(input("Please Enter a valid option: "))
        if key=='1':
            check_list()
            
        elif key=='2':
            replace_number()
            
        elif key=='3':
            replace_name()
        
        elif key=='4':
            find()

        elif key=='5':
            delete_name()

        elif key == "exit":
            print("\nYou have exited the phone directory, see you soon.\n")
            break
        else:
            print("That's not a valid input! Try again")