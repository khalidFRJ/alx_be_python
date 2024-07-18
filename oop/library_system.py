class Book:
    def __init__(self, title: str, author: str):
        self.title = title  
        self.author = author
        
    def __str__(self):
        return f"Book: {self.title} by {self.author}"   


class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count
        
    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

        
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        if isinstance(book, Book):
            self.books.append(book)
            
    def list_books(self):
        for book in self.books:
            print(book)

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





