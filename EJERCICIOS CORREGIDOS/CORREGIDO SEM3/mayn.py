from modulo.EJERCICIO1 import *
from modulo.EJERCICIO2 import *
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

        else:
            print("ERROR \n Vuelva a digitar una opcion")


##---------------PREGUNTA 3--------------------
    print("EJERCICIO 2:")
    print("-----------------------------------------")

    VALOR1=int(input("Ingresar un valor a calcular: "))
    print("Resultado:")
    print("El resultado es: ",multiplicar(VALOR1))


##---------------PREGUNTA 4--------------------
    print("EJERCICIO 3:")
    print("-----------------------------------------")

    