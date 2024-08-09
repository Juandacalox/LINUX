#!/usr/bin/python3	
class Tamaño:
	def __init__(self, tamaño):
		self.__tamaño = tamaño
	def getDetail(self):
		return "el tamaño del cuaderno es: " + self.__tamaño
		
class Hojas:
	def __init__(self, numero):
		self.numero = numero
	def getDetail(self):
		return "el numero de hojas son: "

class Marca:
	def __init__(self, marca):
		self.marca = marca
	def getDetail(self):
		return "Marca es "
class Cuaderno(Tamaño, Hojas, Marca):
	Count = 0
	def __init__(self, tamaño, numero, marca, cuaderno):
		Tamaño.__init__(self, tamaño)
		Hojas.__init__(self, numero)
		Marca.__init__(self, marca)
		self.__cuaderno = cuaderno
		
		Cuaderno.Count +=1
	def getDetail(self):
		return super().getdetail() + "El tamaño es: " + " numero de hojas son: " + " de la marca: " + self.__cuaderno
		
cuaderno = Cuaderno("Grande", 100, "DIsney", "si")

print(cuaderno.getDetail())
print(Cuaderno.Count)
		
