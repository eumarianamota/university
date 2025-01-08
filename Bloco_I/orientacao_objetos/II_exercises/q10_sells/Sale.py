from Product import Product
from ShoppingCart import ShoppingCart
class Sale:
    def __init__(self,client, shopping_cart):
        self.client = client
        self.cart = shopping_cart
    
    def finalize_sale(self):
        print('SUPERMARKET MARIANA')
        for product in self.cart.shopping_cart:
            print(f'{product.name} - {(product.price * product.stock_quantity):.2f}')
        
        price = 0
        for product in self.cart.shopping_cart:
            price += (product.price * product.stock_quantity)
        print(f'TOTAL PRICE: {(price):.2f}')
