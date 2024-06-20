import funciones as fn

pedidos = []

while True:
    try:
        print('***Bienvenido a PaquExpress***')
        print('   1. Registrar pedido')
        print('   2. Listar todos los pedidos')
        print('   3. Imprimir hoja de ruta')
        print('   4. Salir del programa')
        opcion = int(input('Ingrese nº de opciòn: '))
        if opcion == 1:
            fn.registro(pedidos)
        elif opcion == 2:
            fn.lista(pedidos)

            print('')
        elif opcion == 3:
            fn.imprimir(pedidos)
            print('')
        elif opcion == 4: 
            print('Adios')
            break
    except:
        print('Prueba con un valor valido')