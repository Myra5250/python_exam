class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}"

book = Book("The Nobles", "Grace Leister")
print(book.display_info())