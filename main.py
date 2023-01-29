#EJERCICIO 1:

if (__name__=='__main__'):

#Ejercicio 2:
    texto= """Lorem Ipsum es simplemente el texto de relleno de las imprentas y 
archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las
industrias desde el año 1500, cuando unimpresor (N. del T. persona que se 
dedica a la imprenta) desconocido usó una galería de textos y los mezcló de 
tal manera que logró hacer un libro de textos especimen."""

# Split
texto_split=texto.split()
print(texto_split)

# Join
texto_join = " ".join(texto_split)
print(texto_join)

# Count
texto_count = texto.count("texto")
print(texto_count)

# Find
texto_find = texto.find("impresor")
print(texto_find)

# Uppercase
texto_uppercase = texto.upper()
print(texto_uppercase)

# Lowercase
texto_lowercase = texto.lower()
print(texto_lowercase)