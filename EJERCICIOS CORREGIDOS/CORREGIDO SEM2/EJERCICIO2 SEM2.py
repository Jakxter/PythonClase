Biblioteca={
    "Categorias":["Cientifico", "Romance","Comic","bibliografico","ficcion"],
    
    "Usuarios":["ROMMEL", "MONICA", "JULIO", "CARLOS"],

    "Libros": {
        "SOMOS NUESTRO CEREBRO ":{
            "Autor":"Dick Swaab",
            "Categoria":["Cientifico"],
            "CODIGO DE LIBRO":"25-001",
            "Estado":"Disponible"},

        "ROMEO Y JULIETA":{
            "Autor":"William Shakespeare",
            "Categoria":["Romance"],
            "CODIGO DE LIBRO":"25-006",
            "Estado":"Disponible"},

        "SPIDERMAN":{
            "Autor":"Stan lee",
            "Categoria":["Comic"],
            "CODIGO DE LIBRO":"25-015",
            "Estado":"Disponible"},

        "VIDA INTERNA":{
            "Autor":"Dora Mayor",
            "Categoria":["Biograficos"],
            "CODIGO DE LIBRO":"25-024",
            "Estado":"Disponible"},

        "HARRY POTTER":{
            "Autor":"J. K. Rowlingr",
            "Categoria":["Ficcion"],
            "CODIGO DE LIBRO":"25-030",
            "Estado":"Disponible"},
        }
}                    

opcion=0
while opcion != 5:

    print("-----------------------------------------")
    print("""       Menu de la biblioteca:
        1 ---> Consultar Cartegorias de libros
        2 ---> Nombres de los libros y autores
        3 ---> Prestarse un libro
        4 ---> Usuarios
        5 ---> Salir""")
    print("-----------------------------------------")
    opcion = int(input("Selecciona una de las opciones dadas: "))

    
    if opcion == 1:
        print("Las Categorias de libros son:")
        for A in Biblioteca["Categorias"]:
            print("-",A)

    elif opcion == 2:
        for B in Biblioteca["Libros"].keys():
            print("Nombre del libro: ",B)

            Autorlib = Biblioteca["Libros"][B]["Autor"]
            print("Nombre del autor: ",Autorlib)
            print("-----------------------------------------")

    elif opcion == 3:
        
        for C in Biblioteca["Libros"]:
            print(C)

        Libro=list(Biblioteca["Libros"].keys())
        print("-----------------------------------------")
        consulta=input("Ingrese el libro que desee consultar: ").upper()

        if consulta in Libro:

            Estado=Biblioteca["Libros"][consulta]["Estado"]

            if(Estado=="Disponible"):
                print("-----------------------------------------")
                print("El libro esta Disponible")
                print("-----------------------------------------")
                Nombre=input("Ingrese el nombre del usuario al que se le va a prestar el libro: ").upper()
                Usuarios= list(Biblioteca["Usuarios"])

                if(Nombre in Usuarios):
                    Biblioteca["Libros"][consulta]["Estado"]={"Estado":"Prestado"}
                    print(Biblioteca["Libros"][consulta]["Estado"])
                    print("-----------------------------------------")
                    print("Prestamo realizado")
                else:
                    print("-----------------------------------------")
                    print("usuario no existe")
            else:
                print("-----------------------------------------")
                print("No se pudo cambiar de estado, porque el libro no se encuentra disponible")
        else:
            print("-----------------------------------------")
            print("Libro no existe") 

    elif opcion == 4:
        print("-----------------------------------------")
        print("Lista de Usuarios actuales:")
        print(Biblioteca["Usuarios"])

    elif opcion == 5:
        print("-----------------------------------------")
        print("Programa terminado \n Gracias")

    else:
        print("-----------------------------------------")
        print("ERROR \n Vuelva a digitar una opcion")
