#Bernardo Mondragón Ramírez
# Ciclos While (Misión 7)



def numerosDivision():

    print()
    dividendo=int(input("Teclea el dividendo (entero y positivo)"))
    divisor=int(input("Teclea el divisor (entero positivo)"))
    dividir(dividendo,divisor)

def dividir(dividendo,divisor):
    cos=0
    r=dividendo
    residuo=dividendo
    if divisor>0:
        while r>=0:
            r=r-divisor
            if r>=0:
                cos+=1
                residuo=r
        print("%d / %d = %cos, sobra %r"%(dividendo,divisor,cos,residuo))
    else:
        print("Error: Cálculo imposible (teclee números enteros positivos)")

def encontrarMayor():


    nMayor=0
    n=nMayor


    print()
    print("Teclea varios numeros para hallar el Mayor.")
    print("Teclea -1 cuando quieras para terminar")

    if n!= -1:
        while n!= -1:
            if n> 0:
                if n>= nMayor:
                    nMayor= n
            n= int(input("Teclea un numero: "))
        print("Numero mayor es:", nMayor)
    else:
        print("No hay valor mayor")


def main():
    opcion=0
    while opcion != 3:
        print("Bernardo Mondragon Ramirez    A01022325")
        print("Elige una opcion")
        print("""
        1. divisiones.
        2. Numero mayor
        3. Salir""")
        opcion =int(input("Que opcion quieres: "))

        if opcion==1:
            numerosDivision()
        elif opcion==2:
            encontrarMayor()
        elif opcion !=3:
            print("Numero no valido")
    print ("Adios")

main()