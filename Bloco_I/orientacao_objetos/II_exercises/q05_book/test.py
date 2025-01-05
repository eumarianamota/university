from Book import Book
from Library import Library

livro1 = Book('Trono de vidro', 'Sarah J mass')
livro2 = Book('Meu pé de laranja lima', 'Mauro de Vasconcelos')

biblioteca = Library()
biblioteca.lend_book('Trono de vidro')
biblioteca.return_book('Trono de vidro')
biblioteca.list_available_books()
