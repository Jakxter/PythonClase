from modulo.EJERCICIO1 import *
from modulo.EJERCICIO2 import *
from modulo.EJERCICIO4 import *

import sys
import os

if __name__=='__main__':



    print("EJERCICIO 1:")
    print("-----------------------------------------")
    texto= """Lorem Ipsum es simplemente el texto de relleno de las imprentas y 
    archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las
    industrias desde el año 1500, cuando unimpresor (N. del T. persona que se 
    dedica a la imprenta) desconocido usó una galería de textos y los mezcló de 
    tal manera que logró hacer un libro de textos especimen."""
    opcion=0
    print("-----------------------------------------")
    print("Del texto dado: ¿A qué desea convertir?")
    print("-----------------------------------------")
    print(texto)

    while opcion != 7:
        print("-----------------------------------------")
        print("                  Menú                   ")
        print("-----------------------------------------")
        print("1 ---> Texto a Split")
        print("2 ---> Texto a Join")
        print("3 ---> Texto a Count")
        print("4 ---> Texto a Find")
        print("5 ---> Texto a Upper")
        print("6 ---> Texto a Lower")
        print("7 ---> Salir")
        print("-----------------------------------------")
        opcion = int(input("Selecciona una de las opciones dadas: "))
        print("-----------------------------------------")

        if opcion == 1:
            Split(texto)
            print("-----------------------------------------")

        elif opcion == 2:
            Join(texto)
            print("-----------------------------------------")

        elif opcion == 3:
            print("Count: ")
            Count(texto,"texto")
            print("-----------------------------------------")

        elif opcion == 4:
            print("Find: ")
            Find(texto,"impresor")
            print("-----------------------------------------")

        elif opcion == 5:
            Upper(texto)
            print("-----------------------------------------")

        elif opcion == 6:
            Lower(texto)
            print("-----------------------------------------")

        elif opcion == 7:
            print("Programa terminado \n Gracias")
            print("-----------------------------------------")
        else:
            print("ERROR \n Vuelva a digitar una opcion")


##---------------PREGUNTA 3--------------------
    print("EJERCICIO 2:")
    print("-----------------------------------------")

    VALOR1=int(input("Ingresar un valor a calcular: "))
    print("Resultado:")
    print("El resultado es: ",multiplicar(VALOR1))
    print("-----------------------------------------")

##---------------PREGUNTA 4--------------------
    print("EJERCICIO 3:")
    print("-----------------------------------------")

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Catalogo:
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
    
    def mostrar_productos(self):
        for producto in self.productos:
            print(f"Nombre: {producto.nombre} | Precio: {producto.precio}")

catalogo = Catalogo()

producto1 = Producto("Filtro de Aceite", 15.99)
producto2 = Producto("Bujía", 7.49)
producto3 = Producto("Alternador", 129.99)

catalogo.agregar_producto(producto1)
catalogo.agregar_producto(producto2)
catalogo.agregar_producto(producto3)

catalogo.mostrar_productos()
print("-----------------------------------------")

##---------------PREGUNTA 5--------------------
print("EJERCICIO 4:")
print("-----------------------------------------")

Solucion()
print("-----------------------------------------")

##---------------PREGUNTA 6--------------------
print("EJERCICIO 5:")
print("-----------------------------------------")
print(f"\nEl nombre del archivo en ejecucion es: {os.path.basename(sys.argv[0])}")
print("-----------------------------------------")

##---------------PREGUNTA 7--------------------
print("EJERCICIO 6:")
print("-----------------------------------------")
class Producto:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def __str__(self):
        return "Producto: {} ({})".format(self.nombre, self.codigo)

    def identificar_origen(self):
        return self.codigo.split("-")[0]

    def numero_lote(self):
        return self.codigo.split("-")[1]

p1 = Producto("Producto 1", "PERU-0001-2023")
print(p1)
print("País de origen:", p1.identificar_origen())
print("Número de lote:", p1.numero_lote())