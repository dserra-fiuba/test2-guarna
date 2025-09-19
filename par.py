def solicitar_numero():
    return int(input('Ingrese numero positivo para conocer su paridad: '))

def main():
    num = solicitar_numero()

    if (num%2 == 0):
        print('El numero es par.')
    else:
        print('El numero es impar.')

main()