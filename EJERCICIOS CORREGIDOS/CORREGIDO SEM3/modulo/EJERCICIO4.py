import os

def Dividir(num1, num2):
    return float(num1/num2)
    
def SumaN(n):
    if n == 1:
        return 1
    else:
        return n + SumaN(n-1)

def Solucion():
    try:
        Valor2=int(input("Ingrese la cantidad de numeros a sumar: "))
        print("-----------------------------------------")
        print(SumaN(Valor2))
        print("-----------------------------------------")
        Num1=int(input("Ingrese el primer numero a dividir: "))
        Num2=int(input("Ingrese el segundo numero a dividir: "))
        print("-----------------------------------------")
        print(Dividir(Num1, Num2))
        print("-----------------------------------------")
    except:
        print("ERROR")
    else:
        print("Ruta del directorio de trabajo actual: ",os.getcwd())
    finally:
        print("Proceso terminado")

