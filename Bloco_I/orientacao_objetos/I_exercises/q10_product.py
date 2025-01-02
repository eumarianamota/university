# Crie uma classe Product com:
# Atributos:
  # name , price e stock .
# Métodos:
  # buy(quantity) - reduz o estoque (se houver quantidade suficiente).
  # restock(quantity) - aumenta o estoque.
  # show_info() - exibe todas as informações do produto.

# Depois, crie uma classe Store que possui:
  # Um atributo products (lista de objetos Product).
# Métodos:
  # add_product(product) - adiciona um produto na lista.
  # list_products() - exibe todos os produtos e suas informações.

class Product:
  produtos = []

  def __init__(self, name, price, stock):
    self.name = name
    self.price = price
    self.stock = stock

    products = [name, price, stock]

    Product.produtos.append(products)


  def buy(self, quantity):
    if not self.stock >= quantity:
      raise ValueError('A quantidade não pode ser maior que o estoque.')
    self.stock -= quantity
    return self.stock
  
  def restock(self, quantity):
    if not quantity > 0:
      raise ValueError('A quantidade deve ser maior que zero.')
    self.stock += quantity 
    return self.stock
  
  def show_info(self):
    return f'Produto: {self.name} \nValor: R${self.price} \nEstoque: {self.stock} unidades'

class Store:
  def __init__(self):
    self.produtos = Product.produtos

  def add_product(self, name, price, stock):
    product = [name, price, stock]
    self.produtos.append(product)
  
  def list_products(self):
    self.products = self.produtos
    self.intro = ['name', 'price', 'stock']
    largura_colunas = [max(len(str(item)) for item in coluna) for coluna in zip(*self.products, self.intro)]
    cabecalho_formatado = "".join([f"{str(self.intro[i]).ljust(largura_colunas[i] + 2)}" for i in range(len(self.intro))])

    # mostrar a lista 
    print(cabecalho_formatado)
    print("-" * (sum(largura_colunas) + len(self.intro) * 2))

    # mostrar o conteúdo
    for linha in self.products:
        linha_formatada = "".join([f"{str(linha[i]).ljust(largura_colunas[i] + 2)}" for i in range(len(linha))])
        print(linha_formatada)

produto1 = Product('Arroz', 5.99, 20)
produto2 = Product('Feijão', 8.99, 10)
produto3 = Product("Café", 10, 20)

# print(produto1.show_info())
# print(produto2.show_info())
# print(produto3.show_info())

produtos = Store()
produtos.list_products()