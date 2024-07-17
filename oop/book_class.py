class Book:
    def __init__ (self , title:str , author:str , year:int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        del self.title 
        print("Deleting (title of the book)")
    
    def __del__(title):
        print("Deleting (title of the book)")

my_book = Book("1984", "George Orwell", 1949)
print(my_book.__str__())
print(my_book.__repr__())



