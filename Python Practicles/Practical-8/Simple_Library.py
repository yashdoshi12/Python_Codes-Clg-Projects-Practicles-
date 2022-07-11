print("welcome to DBATU's Library!\n")
print("We have the worlds best books collection, all the books listed here are having over 1000 million copies sold. Happy reading!\n")
print("-------------------------------------------------------------------------------------\n")
book_list = {"A Tale of Two Cities":10, "The Lttle prince":10, "Harry Potter and the Philosopher's Stone":10, "And Then There Were None":10, "Dream of the Red Chamber":10, "The Hobbit":10, "The Lion, the Witch and the Wardrobe":10, "She: A History of Adventure":10}

def home_page():
    print(''' Choose any one of the below options,\n
            1. To display available books
            2. To issue a book
            3. To return a book
               Type exit to exit\n''')

def available_books():
    print("The list of available books are: \n")
    available_book_name=[i for i in book_list if book_list[i]>0]
    print(available_book_name, "\n")

def book_issue():
    print("\nYou are in Book Issue section.\n")
    book_select=input("Please enter the book name:")
    if book_select in book_list and book_list[book_select]>0:
        book_list[book_select]-=1
        print("\n",book_select, "has been issued successfully!!!\n")
    else:
        print("\nWe are sorry.", book_select, "is not available at this moment.\n")

def book_return():
    print("\nYou are in Book Return section.\n")
    book_return_name=input("\nEnter the book name to return:")

    if book_return_name in book_list and book_list[book_return_name]<book_list.get(book_return_name):
        book_list[book_return_name]-=1
        print(book_return_name, "has been returned successfully!!!\n")
    else:
        print("We are sorry.", book_return_name, "cant be returned at this moment.\n")

home_page()
while True:
        key=str(input("Please Enter a valid option: "))
        if key=='1':
            available_books()
            
        elif key=='2':
            book_issue()
            
        elif key=='3':
            book_return()
            
        elif key == "exit":
            print("\nYou have exited the library, see you soon.")
            break
        else:
            print("That's not a valid input! Try again")
            