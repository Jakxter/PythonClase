import sys
a=sys.argv

def Argumentos(*args):
    for arg in args:
        print(arg)

Argumentos("Datos personales","Rommel y familia",[2,"primos y",2,"hermanos"],{'Estado civil':["soltero"]})