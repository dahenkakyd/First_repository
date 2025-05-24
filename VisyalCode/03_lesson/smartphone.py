class Smartphone:
	def __init__(self, name_phone, model, namber):
		self.name_phone = name_phone
		self.model = model
		self.namber = namber
	def sayname(self):
		print("марка телефона", self.name_phone)
	def model(self):
		print("модель телефона",self.model )
	def namber(self):
		print("абонентский номер («+79…»)", self.namber)
	def infophone(self):
		print (f, self.name_phone," - ", self.model,".", self.namber)  # type: ignore