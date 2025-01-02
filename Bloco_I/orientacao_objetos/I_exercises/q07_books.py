# Crie uma classe Book com:
# Atributos:
# title e author .
# Outra classe Library com:
# Um atributo books (lista de objetos da classe Book).
# Métodos:
# add_book(book) - adiciona um livro à lista.
# show_books() - exibe todos os títulos disponíveis.

class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author 

class Library:
  def __init__(self):
    self.books = []
  
  def add_book(self, book):
    self.books.append(book)
  
  def show_books(self, books):
    for book in books:
      print(book)