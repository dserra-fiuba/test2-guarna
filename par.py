def solicitar_numero():
    return int(input('Ingrese numero positivo para conocer su paridad: '))

def es_par(num):
    return num%2 == 0

def mostrar_resultado(resultado):
    if (resultado):
        print('El numero es par.')
    else:
        print('El numero es impar.')

def main():
    num = solicitar_numero()
    mostrar_resultado(es_par(num))

main()