"""#  Ejemplo 1 de Funciones
def saludar():
  print("Hola")
saludar()


#  Ejemplo 2 de Funciones
def mostrar_nombre(nombre):
  print(nombre)
  nombre = "stich"
mostrar_nombre("miguel")


#  Ejemplo 3 de Funciones
def suma(valor_uno,valor_dos,valor_tres):
  return valor_uno + valor_dos + valor_tres
resultado = suma(30,20,100)
print(resultado)


#  Ejemplo 4 de Funciones
def division(valor_uno, valor_dos):
  return valor_uno / valor_dos
resultado_division = division(100,2)
print(resultado_division)

#  Ejemplo 5(Usando *)
def ejemplo1(*args):
  print(args)
ejemplo1("Hola","Esto es un ejemplo")

#  Ejemplo 6(Usando **)
def ejemplo2(**args):
  print(args)
ejemplo2(saludo = "Hola", mensaje = "Esto es un mensaje")


#  Ejemplo 7(Usando ambos * y **)
def ejemplo3(*args,**kwargs):
  print(args,kwargs)
ejemplo3("Hola", esto = "es un mensaje")


#  Ejemplo 8()

datos= {}
entrada = ""

while(entrada != "parar"):
  nombre = input("Cuál es tu nombre?: ")
  if(nombre in datos):
    print("Este usuario ya existe")
  else:
    contraseña = input("Cuál es tu contraseña?: ")
    datos[nombre] = contraseña
    entrada = input("Que deseas hacer?: ")
  if(entrada == "parar"):
    print("Hemos terminado")
  elif(entrada == "ver_usuario"):
    print(datos)
  elif(entrada == "borrar_usuario"):
    borrar_usuario = input("Cuál quieres borrar?: ")
    del datos[borrar_usuario]
    print(datos)"""
  

#  Ejemplo 9

"""usuarios = {}

def registrar(nombre, contraseña):
  if (nombre not in usuarios):
    usuario[nombre] = contraseña

while (1<2):
  usuario = input("nombre: ")
  contraseña = input("Contraseña: ")

  registrar(usuario, contraseña)

usuarios = {}

def registrar(nombre, contraseña):
  if (nombre not in usuarios):
    usuarios[nombre] = contraseña

while (1<2):
  nombre = input("Usuario: ")
  contraseña = input("Contraseña: ")
  registrar(nombre, contraseña)
  print(usuarios)

usuarios = {}
def ver_usuarios():
  
  print(usuarios)
ver_usuarios()"""

print("Hola GitHub")