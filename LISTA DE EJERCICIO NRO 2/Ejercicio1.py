opcion=0
Numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
Alumnos = [["Rommel", 20], ["Nely", 17], ["Monica", 15], ["Fausto", 27]]

while opcion != 4:
    print("Menú:")
    print("1. Cuadrado dibujado")
    print("2. Los números multiplos de 2")
    print("3. Alumnos mayores de edad")
    print("4. Salir")
    opcion = int(input("Selecciona una de las opciones dadas: "))

    if opcion == 1:
        Tamaño = 5
        for a in range(Tamaño):
            for b in range(Tamaño):
                print("*", end=" ")
            print()

    elif opcion == 2:
        print("Los numeros multiplos de 2 son: ")
        for num in Numeros:
            if num % 2 == 0:
                print("-",num)

    elif opcion == 3:
        print("Los alumnos mayores de edad son: ")
        for Alumno in Alumnos:
            if Alumno[1] >= 18:
                print("-",Alumno[0])

    elif opcion == 4:
        print("Programa terminado \n Gracias")

    else:
        print("ERROR \n Vuelva a digitar una opcion")