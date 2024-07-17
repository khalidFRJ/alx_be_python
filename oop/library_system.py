class Book:
    def __init__(self,title:str,author:str):
        self.title = title
        self.author = author 

class EBook(Book):
    def __str__(self, file_size:int):
        self.file_size = file_size


class PrintBook(Book):
    def __str__(self, page_count:int):
        self.page_count = page_count

class library(Book) :
    def __str__(self, books = (Book,EBook,PrintBook)):
        self.books = books

    def add_book(self, book):
        self.book = book 
        book.append(Book or PrintBook or EBook)
    def list_books(self):
        print(f"{self.title} and {self.author} and {self.file_size} and {self.page_count}")

    
from library_system import Book, EBook, PrintBook, Library

