
class Vehiculo:
	def __init__(self, marca: str, ruedas: int, color: str, enMarcha: bool = False):
	    self.marca = marca
	    self.ruedas = ruedas
	    self.color = color
	    self.enMarcha = enMarcha

	def arrancar(self):
	    if not self.enMarcha:
	        self.enMarcha = True
	        print("El vehiculo se puso en marcha")

	    else:
	        print("El vehiculo ya estaba en marcha")    


	def tipoVehiculo(self):
	    if self.ruedas == 4:
	        print("Automovil")

	    elif self.ruedas == 2:
	        print("Motocicleta")

	    else:
	        print("El vehiculo debe tener 2 o 4 ruedas")        


	def mostrar(self):
	    for atr, val in vars(self).items():
	        print(f"{atr} : {val}")



vehiculo1 = Vehiculo("Peugeot", 4, "blanco")

vehiculo1.arrancar()

vehiculo1.tipoVehiculo()

vehiculo1.mostrar()

