class Book:
    language = 'ENG'
    is_ebook = True

    def set_title(self,value):
        if not isinstance(value,str):
            raise TypeError('The value of the title attribute mst be of str''type.')
        self.title=value
book = Book()
book.set_title('Python OOPS Exercise')
print(book.title)
