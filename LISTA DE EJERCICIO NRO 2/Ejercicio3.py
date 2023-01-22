Valor1=int(input("Ingrese el primero valor: "))
Valor2=int(input("Ingrese el segundo valor: "))

def Numero(Valor1, Valor2):
    
    if Valor1 > Valor2:
        return Valor1
    else:
        return Valor2

print("El número mayor es: ", Numero(Valor1, Valor2))