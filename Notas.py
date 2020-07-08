import time
Notas = []
ingresar_admin = {"Admin" : "math123"}

def borrar_notas():
	borrar_nombre = input("Ingresa el nombre del estudiante: ")
	borrar_nota = int(input("Ingresa la nota: "))

	if borrar_nombre in Notas and borrar_nota in Notas:
		
		Notas.remove(borrar_nombre)
		Notas.remove(borrar_nota)
		print("Nombre del estudiante y la nota han sido eliminadas con éxito.")

		print()

	else:
		print("Asegúrate de que colocaste una nota ya asignada.")

		print()

def tiempo_espera():
	for x in range(3):
		print (("Registrando{0}").format("."*x), end="\r")
		time.sleep(x)


def ver_notas():
	print(Notas)

registrar_nota = True

while registrar_nota:
	nombre = input("Ingresa tu nombre: ")
	nota = int(input("Cuál fue tu nota?: "))

	if nota >= 9:
		tiempo_espera()
		print("Has sacado A")

	elif nota >= 6:
		tiempo_espera()
		print("Has sacado B")

	elif nota >= 3:
		tiempo_espera()
		print("Has sacado C")

	elif nota < 3:
		tiempo_espera()
		print("Has sacado F")

	else:	
		print("Ingresa tu nota")

	Notas.append(nombre)
	Notas.append(nota)

	ingresar_nota = input("Quieres ingresar otra nota (si/no): ")

	if ingresar_nota.lower() == "si":
		continue 

	elif ingresar_nota.lower() == "no":
		print("¡Hasta luego!")

	print()

	registrar_nota = False

	while not registrar_nota:

		print("Para acceder a más opciones ingresa como administrador")
		usuario = input("Ingresa tu usuario: ")
		contraseña = input("Ingresa la llave: ")
		
		admin = False
		
		while(admin == False):

			if (usuario in ingresar_admin and ingresar_admin[usuario] == contraseña):
				print("Has accedido como administrador")
				ver = input("¿Qué quieres hacer?: ")

				if ver.lower() == "ver notas":
					ver_notas()
					
				elif ver.lower() == "borrar notas":
					borrar_notas()
				 
			else:
				print("Acceso denegado")		
				admin = True
		
	
