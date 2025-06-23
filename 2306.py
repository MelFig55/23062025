import random
import math

trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]
trabajadores2= {}
lista1= {}


def asignar_sueldos():
    global clasificaciones
    for x in trabajadores:
        sueldo = random.randint(300000, 2500000)
        trabajadores2[x] = sueldo
    clasificaciones = ["Sueldos menores a $800.000", "Sueldos entre $800.000 y $2.000.000", "Sueldos superiores a $2.000.000"]
    for trabajador, sueldo in trabajadores2.items():
        if sueldo < 800000:
            clasificacion = clasificaciones[0]
        elif sueldo >= 800000 and sueldo <= 2000000:
            clasificacion = clasificaciones[1]
        else:
            clasificacion = clasificaciones[2]
        trabajadores2[trabajador] = sueldo, clasificacion
        print(f"Trabajador: {trabajador}, sueldo: {sueldo}, clasificacion: {clasificacion}")
    print("Asignacion aleatoria realizada")

def clasificar_sueldos():
    global clasificaciones
    t1 = 0
    t2 = 0
    t3= 0
    total = 0
    for trabajadores, rank in trabajadores2.items():
        if rank[1] == clasificaciones[0]:
            print(f"hola {rank}")
            t1 += 1
            total += rank[0]
        elif rank[1] == clasificaciones[1]:
            print(f"tilin {rank}")
            t2 += 1
            total += rank[0]
        else:
            print(f"chao {rank}")
            t3 += 1
            total += rank[0]

### Despues lo arreglo con los detalles que piden en la guia, tengo la mente en blanco, dejare las bases y despues lo arreglo, no puedo pensar estoy como en blanco, esta todo a la mitad y como de prototipo para testeo
### falta aun


def ver_stats():
    mayor = 0
    menor = None
    for x, y in trabajadores2.values():
        if x > mayor:
            mayor = x
        if menor == None or x < menor:
            menor = x
    valores = [i[0] for i in trabajadores2.values()]
    promedio = sum(valores) / len(valores)

    total= math.prod(valores)
    n = len(valores)
    media_geometrica = total ** (1/n)
    print(f"El sueldo mas alto fue de: ${mayor:.2f} pesos")
    print(f"El sueldo mas bajo fue de: ${menor:.2f} pesos")
    print(f"El promedio de sueldos fue de: ${promedio:.2f} pesos")
    print(f"La media geometrica fue de: ${media_geometrica:.2f} pesos")

def reporte():
    for x, y in trabajadores2.items():
        cantidad = y[0]

def salir():
    input("Saliendo del programa...\nNombre: Melissa Figueroa\nRut: #######\nPresiona enter para continuar")



def menu():
    opcion = 0

    while opcion != 5:
        print("---Menu de sueldos---\n1.Asignar sueldos aleatorios\n2.Clasificar sueldos\n3.Ver estadisticas\n4.Reporte de sueldos\n5.Salir del programa")
        while True:
            try:
                opcion = int(input(""))
                if opcion >= 1 and opcion <= 5:
                    break
                else:
                    print("opcion valida entr e1-5")
            except ValueError:
                print("opcion vañlida entre 1-5")

        if opcion == 1:
            asignar_sueldos()
        elif opcion == 2:
            clasificar_sueldos()
        elif opcion == 3:
            ver_stats()
        elif opcion == 4:
            reporte()
        elif opcion == 5:
            salir()
    

menu()
