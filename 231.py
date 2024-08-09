#!/usr/bin/python
class Vaso:
	def __init__(self, name):
		self.__name = name
	def getDetail(self):
		return "El vaso es: " + self.__name
class Color:
	def __init__(self, color):
		self.__color = color		
class Ancho(Vaso, Color):
	
	Count = 0
	def __init__(self, name, ancho, color):
		Vaso().__init__(self.__name)
		Color().__init__(self.__color)
		self.__ancho = ancho
				
	def getDetail(self, text = ""):
		return super().getDetail + "El vaso es: " + self.__ancho + " El color es:" 
		Ancho.Count += 1
vaso1 = Vaso("circular, 2, naranja")
print(vaso1.getDetail())

vaso2 = Vaso("cuadrado, 4, verde")
print(vaso2.getDetail())
print(Ancho.Count)

