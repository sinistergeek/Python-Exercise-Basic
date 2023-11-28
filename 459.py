class Book:
    language = 'ENG'
    is_ebook = True

book_1 = Book()
book_2 = Book()

book_1.author = 'Edcorner Learning'
book_1.title = 'Python Programming Exercises'

book_2.author = 'Edcorner Learning'
book_2.title = 'Python OOPS Exercises'
book_2.year_of_publishment = 2021

print(book_1.__dict__)
print(book_2.__dict__)
