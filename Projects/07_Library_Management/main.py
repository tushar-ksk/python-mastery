from datetime import date, datetime
def separator():
    print("-"*147)

class Student():
    def __init__(self,name):
        self.name = name
        open(f"{self.name}.txt", 'a').close()
    @property
    def total_books(self):
        with open(f"{self.name}.txt", 'r') as f:
            books_list = f.readlines()
            separator()
            for index, book in enumerate(books_list):
               print(f"{index+1}. {book}".replace("\n","")) 
            separator()


    

    def borrow_books(self, *args: str):

        removed_books = []
        
        # Reading student content
        with open(f"{self.name}.txt", 'r') as stu:
            stu_contents = stu.readlines()
            stu_books = [book.lower().strip() for book in stu_contents]

        # Reading library content
        with open("library.txt", 'r') as lib:
            lib_contents = lib.readlines()
            lib_books = [book.lower().strip() for book in lib_contents]
        print(f"Responce to {self.name}:")
        for arg in args:
            already_have = False
            found_in_library = False
            
            # Check if the student already has the book
            for i, s_book in enumerate(stu_books):
                if arg.lower().strip() == s_book.strip().lower():
                    print(f"{self.name}, You already have a similar book named {stu_contents[i].split(' on 2025')[0]}")
                    already_have = True
                    break
            
            if not already_have:
                for idx, l_books in enumerate(lib_books):
                    if arg.lower() in l_books:
                        found_in_library = True
                    
                        
                        # Giving BOOK TO STUDENT
                        with open(f"{self.name}.txt", 'a') as stu:
                            stu.write(f"{lib_contents[idx].strip()} on {date.today()} at {datetime.now().strftime('%I:%M:%S')}\n")
                        print(f"✔ {lib_contents[idx].strip()} borrowed successfully.")        
                        
                        # Removinging book from library
                        removed_books.append(lib_contents[idx].strip())
                        lib_contents.pop(idx)
                        lib_books.pop(idx)
                        break

                # Writing updated library content to file
                with open("library.txt", 'w') as lib:
                    lib.writelines(lib_contents)

                if not found_in_library:
                    print(f"{arg} NOT found in library.")


        # Printing borrowed books
        if removed_books:
            print(f"\nLibrary books borrowed to {self.name}:")
            for book in removed_books:
                print(f"✔ {book}")
            separator()


    def return_books(self,*args):
        with open(f"{self.name}.txt", 'r') as stu:
            contents = stu.readlines()
            stu_books = [item.lower() for item in contents]
            removed_books = []
            for arg in args:
                found = False
                for idx, book in enumerate(stu_books):
                    if arg.strip().lower() == book.split(" on 2025")[0].strip().lower():
                        removed = contents.pop(idx)
                        stu_books.pop(idx)
                        removed_books.append(removed)
                        found = True
                        
                        break
                
                with open(f"library.txt", 'a') as f:
                
                            f.write(removed)
                if not found:
                    print(f"You don't have any book named {arg}.")


        if removed_books:
            with open(f"{self.name}.txt",'w') as f:
                f.writelines(contents)
            print("Removed books:")
            for book in removed_books:
                print(book.split(" on 2025")[0].strip())
        


tushar = Student("Tushar")

# tushar.borrow_books("anaconda","java","jai mata di","complex number")
# tushar.total_books
# tushar.return_books("The jungle book","Python with tushar")



class library(Student):
    def __init__(self, name):
        self.name = name
    
    @staticmethod
    def registered_student():
        pass
    
    @property
    @staticmethod
    def total_books():
        with open(f"library.txt", 'r') as f:
            books_list = f.readlines()
            separator()
            for index, book in enumerate(books_list):
               print(f"{index+1}. {book}".strip()) 
            separator()


# soham = library("Soham")
# soham.borrow_books("hiMalaya parvat")
# satyam = library("Satyam")
# satyam.borrow_books("anaconda")