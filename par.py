def solicitar_numero():
    return int(input('Ingrese numero positivo para conocer su paridad: '))

def es_par(num):
    return num%2 == 0

def main():
    num = solicitar_numero()
    if (es_par(num)):
        print('El numero es par.')
    else:
        print('El numero es impar.')

main()