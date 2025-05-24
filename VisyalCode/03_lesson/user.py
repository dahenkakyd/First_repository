
class User:

	def __init__(self, first_name, last_name):
		self.username = first_name
		self.surname = last_name

	def sayName(self):
		print("мое имя ", self.username)
	def saysurname(self):
		print("моя фамилия",self.surname )
	def sayname_surname(self):
		print( f"мои имя и фамилия {self.surname} {self.username}")	
