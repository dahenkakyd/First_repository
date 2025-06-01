from address import Address
from mailing import Mailing

to_address = Address(428003, "Чебоксары", "Президентский б-р", 14, 10)
form_address = Address(428028, "Чебоксары", "пр-кт Тракторостроителей", 66, 32)
form_address = Address(428027, "Чебоксары", "Кукшумская", 12, 10)

mailing = Mailing(to_address, from_address, cost=500, track="TR123")
print(mailing)
return f"Отправление {self.track} из {self.from_address} в {self.to_address}. Стоимость {self.cost} рублей."