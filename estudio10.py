"""	Secuencia de Fibonacci
	La serie de Fibonacci es una sucesión infinita de números naturales comenzando del 0 y 1
	Donde se suman los dos valores anteriores 
	Podemos usar como ejemplo 2 conejos, el conejo A se cruza con el conejo B(1+1 = 2)
	Luego de un mes el conejo A da a luz, luego el conejo B y C se cruzan(2+1 = 3)
	Pasa otro mes y el conejo B da a luz, luego el conejo C y D se cruzan(3+2 = 5) y así hasta el infinito..."""



def fibonacci_lento(n):

	if n == 1:
		return 1
	if n == 2:
		return 1
	if n > 2:
		return fibonacci_lento(n-1) + fibonacci_lento(n-2)

for n in range(1,11):
	print(n, ':', fibonacci_lento(n))
"""	Luego de varios cálculos empieza a volverse lento, esto sucede porque
	repite el trabajo cada que lo necesita, por lo que debemos crear un caché
	donde se guarde para luego en un futuro poder usarlo"""

fibonacci_cache = {}

def fibonacci(n):
	#	Si conseguimos el valor entonces lo devuelve.
	if n in fibonacci_cache:
		return fibonacci_cache[n]

	if n == 1:
		value = 1
	elif n == 2:
		value  = 1
	elif n > 2:
		value = fibonacci(n-1) + fibonacci(n-2) #	Guarda el valor y lo devuelve.

	fibonacci_cache[n] = value
	return value

for n in range(1,11):
	print(n, "=", fibonacci(n))


from functools import lru_cache
	#	Desde functools importamos lru_cache(Least recently used cache(Caché Usado recientemente))
@lru_cache(maxsize = 1000)
def fibonacci(n):

				#	Revisa si la entrada es un número positivo

	if type(n) != int:
		raise TypeError("n debe ser un número entero positivo")

	if n < 1:
		raise ValueError("n debe ser un número entero positivo")	

	if n == 1:
		return 1
	if n == 2:
		return 1
	elif n > 2:
		return fibonacci(n-1) + fibonacci(n-2)

for n in range(1,1001):
	print(n, ':', fibonacci(n))

"""for n in range(1,51):
	print(fibonacci(n+1) / fibonacci(n))"""
 
#	Si llamamos a la función con un número negativo,flotante o incluso un 'string', mostrará un error.
print(fibonacci(-1))
