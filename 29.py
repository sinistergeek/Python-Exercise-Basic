import uuid

class Book:
    def __init__(self,title,author):
        self.book_id = self.get_id()
        self.title = title
        self.author = author
    def __repr__(self):
        return f"Book(title='{self.title}',author='{self.author}')"
    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]
book1 = Book('Python Object Oriented Programming Exercise Volume 2','Edcorner Learning')
print(book1)
