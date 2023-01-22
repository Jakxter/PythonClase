import sys

def imprimir_argumentos():
  for argumento in sys.argv[1:]:
    print(argumento)

imprimir_argumentos()