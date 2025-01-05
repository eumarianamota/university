# Classe ParkingLot :
# Atributos: total_spots (número total de vagas), occupied_spots (número atual de vagas ocupadas).
# Métodos:
# vehicle_entry() : Adiciona um veículo, verificando se há vagas disponíveis. Caso o estacionamento esteja cheio, lance uma exceção ParkingLotFullError .
# vehicle_exit() : Remove um veículo, decrementando o número de vagas ocupadas. Caso o estacionamento esteja vazio, lance uma exceção ParkingLotEmptyError .
# show_status() : Exibe o número de vagas disponíveis e ocupadas.

class ParkingLotFullError(Exception):
    pass

class ParkingLotEmptyError(Exception):
    pass

class ParkingLot:
    def __init__(self, total_spots, occupied_spots):
        self.total_spots = total_spots
        self.occupied_spots = occupied_spots
        self.available_spots = total_spots - occupied_spots

    def vehicle_entry(self):
        if self.total_spots == self.occupied_spots:
            raise ParkingLotFullError('O estacionamento está cheio')
        else: 
            self.occupied_spots += 1
    
    def vehicle_exit(self):
        if self.occupied_spots == 0:
            raise ParkingLotEmptyError('Não tem vagas a serem desocupadas')
        else:
            self.occupied_spots -= 1
    
    def show_status(self):
        print(f'AVAILABLE SPOTS: {self.total_spots - self.occupied_spots}')
        print(f'OCCUPIED SPOTS: {self.occupied_spots}')


