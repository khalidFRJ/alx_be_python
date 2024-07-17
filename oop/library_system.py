class Book:
    def __init__(self,title:str,author:str):
        self.title = title
        self.author = author 

<<<<<<< HEAD
class EBook(Book) :
    def __init__(self,fiel_size) :
        self.file_size = fiel_size
        super().__init__(title=str , author=str )

=======
class EBook(Book):
    def __str__(self, file_size:int):
        self.file_size = file_size
        super().__init__(title=str , author=str )


>>>>>>> 17fb3400429441d80d2cbe5d5d7aff98ae6db1d9
class PrintBook(Book):
    def __str__(self, page_count:int):
        self.page_count = page_count

<<<<<<< HEAD
class Library(Book) :
    def __str__(self, books ):
        self.books = []
    
    def add_book(self, book):
        self.book = book 
        book.append(Book or PrintBook or EBook)

    def list_books(self):
        print(f"{self.title} and {self.author} and {self.file_size} and {self.page_count}")


    
=======
class library(Book) :
     def __str__(self, books):
        self.books = []

    def add_book(self, book):
        self.book = book.append(Book or PrintBook or EBook)
        
    def list_books(self):
        print(f"{self.title} and {self.author} and {self.file_size} and {self.page_count}")

    from library_system import Book, EBook, PrintBook, Library


def main():
    my_library = Library()

    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    my_library.list_books()

if __name__ == "__main__":
    main()
>>>>>>> 17fb3400429441d80d2cbe5d5d7aff98ae6db1d9

