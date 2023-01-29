
def multiplicar2(numero):
    return numero*2

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Catalogo:
    def __init__(self):
        self.productos = []
    
    def agregar(self, producto):
        self.productos.append(producto)
    
    def mostrar(self):
        for producto in self.productos:
            print(producto.nombre, producto.precio)

#EJERCICIO 1:

if (__name__=='__main__'):

#EEJERCICIO 2:
    texto= """Lorem Ipsum es simplemente el texto de relleno de las imprentas y 
archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las
industrias desde el año 1500, cuando unimpresor (N. del T. persona que se 
dedica a la imprenta) desconocido usó una galería de textos y los mezcló de 
tal manera que logró hacer un libro de textos especimen."""

    # Split
texto_en_split = texto.split()
print(texto_en_split)

    # Join
texto_en_join = " ".join(texto_en_split)
print(texto_en_join)

    # Count
texto_en_count = texto.count("texto")
print(texto_en_count)

    # Find
texto_en_find = texto.find("impresor")
print(texto_en_find)

    # Uppercase
texto_en_uppercase = texto.upper()
print(texto_en_uppercase)

    # Lowercase
texto_en_lowercase = texto.lower()
print(texto_en_lowercase)

#EJERCICIO 3:
num = 7
print(multiplicar2(num))

#EJERCICIO 4:
catalogo = Catalogo()
catalogo.agregar(Producto("Toyota", 15000))
catalogo.agregar(Producto("Audi", 140000))
catalogo.agregar(Producto("BMV", 14000))
catalogo.agregar(Producto("Nissan", 13500))
catalogo.agregar(Producto("Ferrari", 20000))
catalogo.agregar(Producto("Onda", 9000))
catalogo.mostrar()