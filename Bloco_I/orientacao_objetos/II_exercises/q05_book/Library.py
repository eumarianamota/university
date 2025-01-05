from Book import Book

class BookUnavailableError(Exception):
  pass

class BookNotBorrowedError(Exception):
  pass

class Library:
  def __init__(self):
    self.books = Book.book
  
  def lend_book(self, book):
    for i in self.books:
      if book == i[0]:
        if i[-1] == 'Borrowed':
          raise BookUnavailableError('O livro não está disponível para empréstimo')
        else:
          i[-1] = 'Borrowed'
  
  def return_book(self, book):
    for i in self.books:
      if book == i[0]:
        if i[-1] == 'Available':
          raise BookNotBorrowedError('O livro não foi emprestado')
        else:
          i[-1] = 'Available'

  def list_available_books(self):
    for i in self.books:
      if i[-1] == 'Available':
        print(f'{i[0]} | {i[1]} | {i[2]}')