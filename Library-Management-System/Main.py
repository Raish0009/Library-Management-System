import json
class Library:
    Books=[]
    BorrowedBook=[]
    path=rf"F:\indixpert-Python\Library-Management-System\Books.json"
    path2=rf"F:\indixpert-Python\Library-Management-System\Borrowed-Books.json"
    def __init__(self):
        pass
    def menu(self):
        print("Press 1 - Add Book")
        print("Press 2 - Borrow Book")
        print("Press 3 - Return Book")
        print("Press 4 - Exit")

        choice=int(input("Enter your choice :"))
        data=Library()
        if choice==1:
            data.AddBook()
        elif choice==2:
            data.BorrowBook()
        elif choice==3:
            data.ReturnBook()
        elif choice==4:
            exit()
        else:
            print("Please enter valid choice")
            data.menu()
            

    
    def AddBook(self):
        BooksData={}
        BooksData['id']=int(input("Enter Book id :"))
        BooksData['title']=input("Enter Book title :")
        BooksData['author']=input("Enter Book author :")
        BooksData['category']=input("Enter Book category :")
        data=Library()
        data.Books.append(BooksData)
        libraryData=json.dumps(data.Books,indent=4)
        with open(data.path,"w") as file:
            file.write(libraryData)
        print("Book added successfully in library")
        data.menu()
    
    def BorrowBook(self):
        data=Library()
        with open(data.path,"r") as file:
            Available=json.load(file)
            print("** Available Books in library **")
            AvailableData=json.dumps(Available,indent=4)
            print(json.dumps(Available,indent=4))

        choice=int(input("Which book you want to borrow :"))
        # choice=input("Which book you want to borrow :")

        for book in Available:
            for key,value in book.items():
                if value==choice:
                    Your_Book=json.dumps(book,indent=4)
                    print(Your_Book)
                    data.BorrowedBook.append(book)

        with open(data.path2,"w") as file:
            Books=json.dumps(data.BorrowedBook,indent=4)
            file.write(Books)

        data.Books.append(Available)
        
        for myBook in data.Books:
            for myBooks in myBook:
                for key,value in myBooks.items():
                    if value==choice:
                        print("mybook :- ",myBooks)
                        # data.Books.remove(myBooks)
                        # libraryData=json.dumps(data.Books,indent=4)
                        # with open(data.path,"w") as file:
                        #     file.write(libraryData)

        print(f"Book borrowed\nBook id : {choice}")

        data.menu()

    def ReturnBook(self):
        print("Book returned")



data=Library()
data.menu()