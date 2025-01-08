from Product import Product 

def main():
    arroz = Product('arroz', 12, "01/04/2006")
    arroz.add_stock(30)
    arroz.show_stock()
    arroz.check_expiry('01/02/2006')

if __name__ == '__main__':
    main()