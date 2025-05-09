def funcA():
	print("Начали делать А")
	funcB()
	print("Закончили делать А")

def funcB():
	print("Начали делать В")
	funcC()
	print("Закончили делать В")

def funcC():
	print("Начали делать С")
	funcD()
	print("Закончили делать С")

def funcD():
	print("Сделали D")

print("Начали программу")
funcA()
print("Закончили программу")