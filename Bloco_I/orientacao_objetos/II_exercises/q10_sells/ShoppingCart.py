class InsufficientStockError(Exception):
    pass

class ProductNotInCartError(Exception):
    pass

class ShoppingCart:
    def __init__(self):
        self.shopping_cart = []
    
    def add_product(self, product, quantity):
        if product.stock_quantity < quantity:
            raise InsufficientStockError('Insufficient Stock Error')
        self.shopping_cart.append(product)
    
    def remove_product(self, product_name):
        for product in self.shopping_cart:
            if product.name == product_name:
                return self.shopping_cart.remove(product_name)
            raise ProductNotInCartError('Product Not In Cart Error')
    
    def calculate_total(self):
        price = 0
        for product in self.shopping_cart:
            price += (product.price * product.stock_quantity)
        return price