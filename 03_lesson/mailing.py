from address import Address
class Mailing:
    def __init__ (self, to_address,from_address, cost, track):
        self.to_address=to_address
        self.from_address= from_address
        self.cost=cost
        self.track=track
    def __str__(self):
        # self.to_address = ", ".join([str(Address) for Address in self.to_address])
        return (f"Отправление {self.track} из {self.to_address} в {self.from_address}. Стоимость {self.cost} рублей.")