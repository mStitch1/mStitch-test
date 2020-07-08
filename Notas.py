import time
Notas = []
Ingresar_admin = {"Admin" : 123}

def borrar_nota():
	
	borrar = input("¿Cuál quieres borrar?: ")
	if borrar in Notas:
		del Notas[borrar]
		print("Nota borrada con éxito")
	else:
		print("Asegúrate que colocaste una nota que ya está.")

def tiempo_espera():
	for v in range(1,4):
		time.sleep(1)
		print("Registrando...")

def ver_notas():
	for k,v in Notas():
		print("Nombre = ", k)
		print("Nota = ", v)

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
		print("Está bien")

	registrar_nota = False

	while not registrar_nota:

		print("Para acceder a más opciones ingresa como administrador")
		usuario = input("Ingresa tu usuario: ")
		contraseña = int(input("Ingresa la llave: "))
		Ingresar_admin[usuario] = contraseña
		admin = False

		while not admin:

			if usuario in Ingresar_admin and Ingresar_admin[usuario] == contraseña:
				print("Has accedido como administrador")
			ver = input("¿Qué quieres hacer?: ")
			if ver.lower() == "ver_notas":
				ver_notas()
				continue

			elif ver.lower() == "borrar_notas":
				borrar_nota()
				continue	
				admin = True

			else:
				print("Acceso denegado")
