class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        
class EBook(Book):
    def __init__(self, title, author, pages, file_format):
        super().__init__(title, author, pages)
        self.file_format = file_format

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}, Format: {self.file_format}"

ebook = EBook("The Nobles", "Grace Leister", 200, "csv")
print(ebook.display_info())