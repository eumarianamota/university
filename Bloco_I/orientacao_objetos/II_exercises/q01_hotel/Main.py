from Hotel import Hotel

def main():
    palace = Hotel(101, 102, 103, 104, 105, 106, 107, 108, 109, 110)
    palace.check_in(107)
    palace.check_in(105)
    palace.check_in(103)
    palace.show_status()

if __name__ == '__main__':
    main()