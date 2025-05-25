class Smartphone:
	def __init__(self, name_phone, model, number):
		self.name_phone = name_phone
		self.model = model
		self.number = number
	def sayname(self):
		print("марка телефона", self.name_phone)
	def model(self):
		print("модель телефона",self.model )
	def number(self):
		print("абонентский номер («+79…»)", self.number)
	def infophone(self):
		print (f"{self.name_phone}  - {self.model} . {self.number}")  