import sys

codigo=(input("Digite los argumentos a ingresar: "))

def Argumentos(*args):
    for arg in args:
        print(arg)
        
Argumentos(codigo)