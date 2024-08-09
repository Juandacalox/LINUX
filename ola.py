#!/usr/bin/python3
class Drink:
   def __init__(self, name):
      self.__name = name
   def getDetail(self):
   	return"la bebida es: " + self.__name

drink = Drink("agua")
print(drink.getDetail())

class Product:
	def __init__(self, cost, price):
		self.cost = cost
		self.price = price
	def getGain(self):
		return self.price - self.cost
	
class Beer(Drink, Product):

	Count = 0
	
	def __init__(self, name, brand, alcohol, cost, price):
		Drink.__init__ (self, name)
		Product.__init__(self, cost, price)
		self.__brand = brand 
		self.__alcohol = alcohol 
		Beer.Count += 1
	def getDetail(self):
		return super().getDetail() + "de la marca: " + self.__brand + " y el alcohol: " + str(self.__alcohol)

	@staticmethod
	def getClassInfo():
		return "Se han creado " + str(Beer.Count) + " objeto"
beer1 = Beer("Pale Ale", "Minerva", 4.5, 10, 40)
print(beer1.getDetail())
print(beer1.getGain())
beer2 = Beer("Stout", "Minerva", 6, 12, 201)
print(beer2.getDetail())
print(beer2.getGain())
print(Beer.Count)
print(Beer.getClassInfo())
