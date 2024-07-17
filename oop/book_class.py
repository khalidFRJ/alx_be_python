class Book:
    def __init__ (self , title:str , author:str , year:int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

<<<<<<< HEAD
    
    def __del__(self):
        print(f"Deleting {self.title}")
=======
    def __del__(self):
        del self.title
        print("Deleting (title of the book)")
>>>>>>> 46ebf376f20da74a18297c81545b4e79c73918ee

my_book = Book("1984", "George Orwell", 1949)
print(my_book.__str__())
print(repr(my_book))
del my_book



