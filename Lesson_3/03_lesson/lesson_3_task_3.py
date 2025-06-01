from address import Address
from mailing import Mailing

to_address = Address(428003, "Чебоксары", "Президентский б-р", 14, 10)
from_address = Address(428028, "Чебоксары", "пр-кт Тракторостроителей", 66, 32)

mailing = Mailing(to_address, from_address, cost=500, track="TR123")
print(mailing)