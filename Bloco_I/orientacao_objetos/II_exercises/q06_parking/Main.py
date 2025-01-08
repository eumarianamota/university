from ParkingLot import ParkingLot

def main():
    shopping = ParkingLot(100, 50)
    shopping.vehicle_entry()
    shopping.vehicle_entry()
    shopping.vehicle_entry()
    shopping.vehicle_entry()
    shopping.vehicle_entry()
    shopping.vehicle_exit()
    shopping.vehicle_exit()
    shopping.show_status()

if __name__ == '__main__':
    main()