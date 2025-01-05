# Classe Book :
# Atributos: title , author , status ( "available" ou "borrowed" ).
# 2. Classe Library :
# Atributos: Uma lista de objetos Book .
# Métodos:
# lend_book(title) : Marca o livro como "borrowed" , verificando se está "available" . Caso não esteja disponível, lance uma exceção
# BookUnavailableError .
# return_book(title) : Marca o livro como "available" . Caso o livro não tenha sido emprestado, lance uma exceção
# BookNotBorrowedError .
# list_available_books() : Mostra os livros disponíveis para empréstimo.