##NOMBRE: ROMMEL FAUSTO AUQUI GAMBOA
##---------------PREGUNTA 1--------------------
print("EJERCICIO 1:")
print("-----------------------------------------")

nombre = input("Ingrese su Nombre: ")
apellido = input("Ingrese sus apellidos completos: ")
edad = input("Ingrese su edad en años: ")
telefono =input("Ingrese su numero telefonico: +51- ")
direccion = input("Ingrese la direccion de su vivienda: ")
sexo = input("Ingrese su Sexo (Masculino, Fenenino, Otro): ")

print("-----------------------------------------")
print("SUS DATOS PERSONALES SON: ")
print("Su nombre completo es: ",nombre , apellido)
print("Su edad es: ",edad,"años")
print("Su telefono es: ",telefono)
print("Su direccion es: ",direccion)
print("Su sexo es: ",sexo)

print("\n")

##---------------PREGUNTA 2--------------------
print("EJERCICIO 2")
print("-----------------------------------------")
import math

print("CALCULAR AREAS:")
Radio=float(input("Ingrese el Radio: "))

Area_triangulo=Radio*Radio/2
Area_circulo= math.pi*Radio**2
Area_cuadrado=Radio**2
print("-----------------------------------------")
print("RESULTADO: ")
print("El area del triangulo es:",Area_triangulo)
print("El area del ciculo es:",Area_circulo)
print("El area del cuadrado es:",Area_cuadrado)

print("\n")

##---------------PREGUNTA 3--------------------
print("EJERCICIO 3")
print("-----------------------------------------")

Valor1=float(input("Ingrese el primer valor: "))
Valor2=float(input("Ingrese el segundo valor: "))
Valor3=float(input("Ingrese el tercer valor: "))

Suma = Valor1+Valor2+Valor3
Resta = Valor1-Valor3-Valor3
Multiplicacion = Valor1*Valor2*Valor3
Division= Valor1/Valor2/Valor3
Division_Entera= Valor1//Valor2//Valor3

print("-----------------------------------------")
print("RESULTADO: ")

print("El valor de la suma es: ",Suma)
print("El valor de la resta es: ",Resta)
print("El valor de la multiplicacion es es: ",Multiplicacion)
print("El valor de la division es: ",Division)
print("El valor de la division entera es: ",Division_Entera)

print("\n")

##---------------PREGUNTA 4--------------------
print("EJERCICIO 4")
print("-----------------------------------------")

Dato= input("Ingrese un valor: ")

print("-----------------------------------------")
print("RESULTADO: ")

print(f"-----> El tipo de dato es: {type(Dato)}")

print("\n")

##---------------PREGUNTA 5--------------------
print("EJERCICIO 5")
print("-----------------------------------------")

import sys
ubicacion = sys.argv[0]

print("-----------------------------------------")
print("RESULTADO: ")

print("La ubicacion de la carpeta es: ", ubicacion)

print("\n")

##---------------PREGUNTA 6--------------------
print("EJERCICIO 6")
print("-----------------------------------------")

N_veces=int(input("Ingrese la cantidad de veces que quiera sumar: "))
Suma_6 = 0
for i in range(1, N_veces+1):
    Suma_6 += i

print("-----------------------------------------")
print("RESULTADO: ")

print("La suma es:", Suma_6)

print("\n")

##---------------PREGUNTA 7--------------------
print("EJERCICIO 7")
print("-----------------------------------------")

Numero01=int(input("Ingrese el primer valor: "))
Numero02=int(input("ingrese el segundo: valor: "))

if Numero01==Numero02:
    print("---> La igualdad de los 2 valores es verdadera")
elif Numero01!=Numero02:
    print("---> La desigualdad de los 2 valores es verdadera")

    if Numero01>Numero02:
        print("---> El primer valor es mayor ")
    elif Numero02>=Numero01:
        print("---> El segundo es mayor igual que el primero")

print("\n")

##---------------PREGUNTA 8--------------------
print("EJERCICIO 8")
print("-----------------------------------------")

Contraseña=input("ingrese la contraseña que desee almacenar: ")
ContraIntro=input("Por favor ingrese su contraseña: ")

Original=Contraseña.lower()
Copia=ContraIntro.lower()

print("-----------------------------------------")
print("RESULTADO: ")

if Original==Copia:
    print("Ingreso bien su contraseña")
else:
    print("Ingreso mal su contraseña")