import json
class Library:
    Books=[]
    BorrowedBook=[]
    path=rf"E:\Library-Management-System\Library-Management-System\Books.json"
    path2=rf"E:\Library-Management-System\Library-Management-System\Borrowed-Books.json"
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
            print(json.dumps(Available,indent=4))

        choice=int(input("Which book you want to borrow :"))

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
        
        filtered_data = [d for d in Available if choice not in d.values()]

        libraryData=json.dumps(filtered_data,indent=4)
        with open(data.path,"w") as file:
            file.write(libraryData)

        print(f"Book borrowed\nBook id : {choice}")

        data.menu()

    def ReturnBook(self):

        data=Library()
        with open(data.path2,"r") as file:
            Borrowed=json.load(file)
            print(json.dumps(Borrowed,indent=4))
        
        choice=int(input("Which book you want to return :"))

        with open(data.path,"r") as file:
            AvailableBooks=json.load(file)
            data.Books=AvailableBooks

        for book in Borrowed:
            for key,value in book.items():
                if value==choice:
                    data.Books.append(book)

        with open(data.path,"w") as file:
            Books=json.dumps(data.Books,indent=4)
            file.write(Books)

        filtered_data = [d for d in Borrowed if choice not in d.values()]

        libraryData=json.dumps(filtered_data,indent=4)
        with open(data.path2,"w") as file:
            file.write(libraryData)

        data.menu()

data=Library()
data.menu()