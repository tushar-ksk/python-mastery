def return_book(self,*args):
    with open(f"{self.name}.txt", 'r') as stu:
        contents = stu.readlines()
        stu_books = [item.lower() for item in contents]
        removed_books = []
        for arg in args:
            found = False
            for idx, book in enumerate(stu_books):
                if arg.strip().lower() == book.strip().lower():
                    removed = contents.pop(idx)
                    stu_books.pop(idx)
                    with open(f"{self.name}.txt",'w') as f:
                        f.writelines(contents)
                    removed_books.append(removed)
                    found = True
                    with open(f"library.txt", 'a') as f:
                        f.write(removed)
                    break

            if not found:
                print(f"You don't have any book named {arg}.")


    if removed_books:
        print("Removed books:")
        for book in removed_books:
            print(book)