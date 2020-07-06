import itertools


def ganador(juego_actual):

	def todos_iguales(l):
		if l.count(l[0]) == len(l) and l[0] != 0:
			return True
		else:
			return False

	for row in tabla:

		if todos_iguales(row):
			print(f"El jugador {row[0]} gana horizontalmente. (-)")
			return True

	#	Diagonal

	diags = []

	for col, row in enumerate(reversed(range(len(tabla)))):
		diags.append(tabla[row][col])

	if todos_iguales(diags):
		print(f"El jugador {diags[0]} gana diagonalmente. (/)")
		return True



	diags = []

	for ix in range(len(tabla)):
		diags.append(tabla[ix][ix])

	if todos_iguales(diags):
		print(f"El jugador {diags[0]} gana diagonalmente. (\\)")
		return True




	#	Vertical

	for col in range(len(tabla)):
		check = []


		for row in tabla:
			check.append(row[col])

		if todos_iguales(check):
			print(f"El jugador {check[0]} gana verticalmente. (|)")
			return True
	return False


def tablero(tabla_map, player = 0, fila = 0, columna = 0, just_display = True):
	try:
		if tabla_map[fila][columna]:
			print("Esta posición ya está ocupada. Elige otra")
			return tabla_map, False

		print("   0, 1, 2")

		if not just_display:
			tabla_map[fila][columna] = player

		for count, row in enumerate(tabla_map):
			print(count, row)
		
		return tabla_map, True

	except IndexError as e:
		print("Asegurate de que colocaste 0, 1 o 2 en fila/columna", e)
		return tabla_map, False
	except Exception as e:
		print("Algo ha salido mal:(", e)
		return tabla_map, False

jugar = True
player = [1, 2]

while jugar:
	tabla = [[0, 0, 0],
			 [0, 0, 0],
			 [0, 0, 0]]

	ganador_del_juego = False
	tabla, _ = tablero(tabla, just_display = True)
	elige_jugador = itertools.cycle([1, 2])
		 
	while not ganador_del_juego:
		jugador = next(elige_jugador)
		print(f"Jugador {jugador}")
		jugado = False


		while not jugado:
			fila = int(input("¿A cuál fila juegas? (0, 1, 2): "))
			columna = int(input("¿A cuál columna juegas? (0, 1, 2): "))
			tabla, jugado = tablero(tabla, jugador, fila, columna)


		if ganador(tabla):
			juego_terminado = True
			otra_vez = input("Quieres jugar otra vez? (si/no): ")

			if otra_vez.lower() == "si":
				print("Reiniciando")

			elif otra_vez.lower() == "no":
				print("Espero hayas disfrutado el juego. ¡Hasta luego!")	
				jugar = False

			else:
				print("Huh?, Supongo que no quieres jugar.")
				jugar = False




