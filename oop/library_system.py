class Book:
    def __init__(self,title:str,author:str):
        self.title = title
        self.author = author 

class EBook(Book):
    def __str__(self, file_size:int):
        self.file_size = file_size
        super().__init__(title=str , author=str )


class PrintBook(Book):
    def __str__(self, page_count:int):
        self.page_count = page_count

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

