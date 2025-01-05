from Product import Product 

arroz = Product('arroz', 12, "01/04/2006")
arroz.add_stock(30)
arroz.show_stock()
arroz.check_expiry('01/02/2006')