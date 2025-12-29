from main import separator, datetime, date


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
                if arg.lower() in s_book:
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