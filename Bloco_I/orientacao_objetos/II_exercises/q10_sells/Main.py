from Product import Product 
from Sale import Sale 
from ShoppingCart import ShoppingCart

def main():
    produto1 = Product('arroz', 3.99, 10)
    produto2 = Product('açucar', 3.99, 10)
    produto3 = Product('linguiça calabresa', 3.99, 10)
    produto4 = Product('pote de doce de leite em conserva', 3.99, 10)

    cart = ShoppingCart()
    cart.add_product(produto1, 5)
    cart.add_product(produto2, 5)
    cart.add_product(produto3, 5)
    cart.add_product(produto4, 5)

    sale = Sale('mariana', cart)
    sale.finalize_sale()

if __name__ == '__main__':
    main()

