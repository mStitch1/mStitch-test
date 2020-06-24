#  Ejemplo 1 de Funciones
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


"""#  Ejemplo 8

datos= {}
entrada = ""

while(1<2):
  entrada = input("Que deseas hacer?: ")

  if (not entrada):
      print ("Estos son los comandos: \nregistrarme\nparar\nborrar_usuario\nver_usuario")
      continue

  if(entrada == "registrarme"):
      # solo te va a pedir si se cumple arriba
    nombre = input("Cuál es tu nombre?: ")

    if(nombre in datos):
        print("Este usuario ya existe")
        continue

    contraseña = input("Cuál es tu contraseña?: ")
    datos[nombre] = contraseña

  elif(entrada == "parar"): # si no es registrar entonces es parar?
    print("Hemos terminado") #muestra y para
    break

  elif(entrada == "ver_usuario"):
    print("Estos son los usuarios registrados", datos) 

  elif(entrada == "borrar_usuario"):
    borrar_usuario = input("Cuál quieres borrar?: ")

    if(borrar_usuario not in datos):
      print("Este usuario no existe")

    elif(borrar_usuario in datos):
      del datos[borrar_usuario]
      print("El usuario ha sido borrado con éxito", datos)
"""  #Ignorar


#  Ejemplo 9

usuarios = {} 
entrada = ""

def registrar(nombre, contraseña):
  if (nombre not in usuarios): 
    usuarios[nombre] = contraseña


def ver_usuarios():
  print("Estos son los usuarios registrados -->", usuarios)


def borrar_usuario():
    borrar_usuario = input("Cuál quieres borrar?: ")


    if(borrar_usuario not in usuarios):
      print("Este usuario no existe")


    elif(borrar_usuario in usuarios):
      del usuarios[borrar_usuario] 
      print("¡El usuario ha sido borrado con éxito!")


while (1<2):
  entrada = input("¿Que hacemos?: ")
  if (entrada != "registrarme","ver_usuarios","borrar_usuario","parar"):

      print("Coloca un comando: \nregistrarme\nver_usuario\nborrar_usuario\nparar")
      continue



  if(entrada == "registrarme"):
    nombre = input("¿Cuál es tu nombre?: ")


    if(nombre in usuarios):
        print("Este usuario ya existe")
        continue


    if (len(nombre) < 3):
        print("Tu nombre debe tener más de 3 carácteres")
        continue


    elif(len(nombre) > 15):
        print("Tu nombre no puede tener más de 15 carácteres")
        continue


    contraseña = input("¿Cuál es tu contraseña?: ")

    registrar(nombre, contraseña) #Recuerda el orden <- esto también
    print("¡Te has registrado con éxito!")

  if(entrada == "parar"):
      print("¡Hemos terminado!")
      break


  if(entrada == "ver_usuarios"):
      ver_usuarios() # asi ctmr : v si no pones () 


  elif(entrada == "borrar_usuario"):
      borrar_usuario()

  print ("\n")
