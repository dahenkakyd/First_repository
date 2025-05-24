from address import Address
from Mailing import Mailing

to_address = to_address(428003, "Чебоксары", "Президентский б-р", 14, 10)
form_address1 = from_address(428028, "Чебоксары", "пр-кт Тракторостроителей", 66, 32)
form_address2 = from_address(428027, "Чебоксары", "Кукшумская", 12, 10)

Mailing = mailing(to_address, [from_address1, from_address2])
print(Mailing)
print ( f"Отправление {self.track} из {self.to_address} в {self.from_address}. Стоимость {self.cost}.")