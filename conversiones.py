#importamos la libreria math
import math

#se crean las funciones de las operaciones
def dolar(num1):
    return num1*0.052

def libras(num1):
    return num1*0.039

def argentinos(num1):
    return num1*50.15

def bolivares(num1):
    return num1*1.91

def euros(num1):
    return num1*0.047

#indicamos las opciones en el menu
while True:
    print("calculadora basica")
    print("elija una opcion")
    print("a) pesos a dolares")
    print("b) pesos a libras esterlinas")
    print("c) pesos a pesos argentinos")
    print("d) pesos a bolivares")
    print("e) pesos a euros")
    print("f) salir")

     #pedimos la opcion al usuario
    opcion=input("ingrese la opcion(a,b,c,d,e,f):")

    #ejecutamos la operacion correspondiente
    if opcion in ["a","b","c","d","e"]:
        num1=float(input("ingresar el primer numero: "))

        if opcion=="a":
            resultado=dolar(num1)
            print("el resultado de la multiplicacion es: ",resultado)

        elif opcion=="b":
            resultado=libras(num1)
            print("el resultado de la multiplicacion es: ",resultado)

        elif opcion=="c":
            resultado=argentinos(num1)
            print("el resultado de la multiplicacion es: ",resultado)

        elif opcion=="d":
            resultado=bolivares(num1)
            print("el resultado de la multiplicacion es: ",resultado)

        elif opcion=="e":
            resultado=euros(num1)
            print("el resultado de la multiplicacion es: ",resultado)

    elif opcion=="f":
        print("saliendo del programa")
        break
    else:
        print("opcion invalida")

    input("presiona enter para continuar...")


        