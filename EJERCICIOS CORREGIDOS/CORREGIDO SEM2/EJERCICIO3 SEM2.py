#funcion a utlizar
def MAYOROMENOR(Valor1,Valor2):
    if Valor1>Valor2:
        return Valor1
    else:
        return Valor2

print("-----------------------------------------")
NUM1=int(input("Ingrese el primer valor: "))
NUM2=int(input("Ingrese el segundo valor: "))
print("-----------------------------------------")
print("El numero mayor de los ingresados es: ",MAYOROMENOR(NUM1,NUM2))
