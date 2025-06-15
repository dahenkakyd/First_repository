class Smartphone:
	def __init__(self, name_phone, model, number):
		self.name_phone = name_phone
		self.model = model
		self.number = number
	def sayname(self):
		print("марка телефона", self.name_phone)
	def get_model(self):
		return self.model
	def get_number(self):
		return self.namber
	def infophone(self):
		print (f"{self.name_phone}  - {self.model} . {self.number}")  