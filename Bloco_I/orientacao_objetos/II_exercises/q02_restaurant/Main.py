from Item import Item
from Order import Order
from Bill import Bill

def main():
    item1 = Item('pizza', 30)
    item2 = Item('batata', 15)
    item3 = Item('refri', 5)

    pedidos = Order()
    pedidos.add_item(item1)
    pedidos.add_item(item2)
    pedidos.add_item(item3)

    pedidos.remove_item(item3)

    conta = Bill(pedidos)
    conta.calculate_total()
    conta.show_bill()

if __name__ == '__main__':
    main()

