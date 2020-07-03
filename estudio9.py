import datetime
import logging

# Tuplas 

datos_tupla = ("Miguel", "Quintero", 18, True)
nombre, apellido, edad, vivo_muerto = datos_tupla

print()

# Diccionario

datos_diccionario = {"Nombre" : "Francisco", "Apellido" : "Hernández", "Edad" : 20}
datos_diccionario["¿Habla 2 o más idiomas?"] = False
for k,v in datos_diccionario.items():
	print(k," = ",v)

# - - - - - - - - - - - - - - - - - - - - Funciones - - - - - - - - - - - - - - - - - - - - 
  

def pregunta():
	print("Los familiares le preguntan al médico forense a qué hora sucedió esto") 

def informacion():

	LOG_FORMAT = "%(levelname)s %(message)s - %(asctime)s"
	logging.basicConfig(filename = "Informacion.Log", level=logging.INFO,format = LOG_FORMAT)
	logger = logging.getLogger()
	logger.info("El sujeto Miguel fue asesinado")
	print(logger.level)



def hora():
	fecha = datetime.date(2020,7,3)
	print(fecha.strftime("%A,%B %d, %Y"))
	reloj = datetime.datetime.now()
	print("El suceso fue el día",reloj.day,"de Julio")


# - - - - - - - - - - - - - - - - - - - - Fin de Funciones - - - - - - - - - - - - - - - - - - - - #

# - - - - - - - - - - - - - - - - - - - - Condicionales - - - - - - - - - - - - - - - - - - - - # 

while(1<2):
	alerta = input("Estás siendo seguido, ¿Qué haces?: ")

	print(
"Correr",
"Parar",
"Esconderte",
"Luchar")

# Toma tus decisiones

	if alerta not in ["Correr", "Parar", "Esconderte"]:
		print("¡Cada vez están más cerca!")

	if alerta == "Correr":
		print("Sigues derecho...")

		luz = input("Se ve una luz a la lejanía, ¿sigues corriendo hacía ella?: ")
		if(luz == "Si"):

			print("Te has encontrado con la policía y ahora estás salvo.")
			break
			
		else:
			print("Fuiste alcanzado y derrotado.",
"La policía llega al lugar y revisa a la víctima...")

			print("Nombre = ",nombre)
			print("Apellido = ", apellido)
			print("Edad =", edad)
			print("¿Está muerto? = ", vivo_muerto)

			informacion()
			break



	elif alerta == "Parar":
		print("Has parado")
		duda = input("Luego de que paraste ellos empiezan a correr hacia a ti,¿Qué haces?: ")

		if(duda == "Correr"):
			luz = input("Se ve una luz a la lejanía, ¿sigues corriendo hacía ella?: ")

			if(luz == "Si"):
				print("Te has encontrado con la policía y ahora estás salvo.")
				break

	elif alerta == "Esconderte":
		print("Te has escondido y has pasado desapercibido")
		print("Lamentablemente al salir ellos te están esperando y no queda más que pelear contra ellos.")
		pelear = input("¿Peleas o tratas de defenderte?: ")

		if pelear == "Pelear":
			print("Peleaste y diste lo mejor de ti pero eran demasiados")

		else:
			print("Hayas hecho lo que hayas hecho igual no podrías contra ellos...")
			print("Una persona llega al lugar y encuentra el cuerpo y procede a llamar a la policía")
			pregunta()
			hora()


