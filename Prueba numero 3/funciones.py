


sectores = ['norte', 'centro', 'sur']

'''

Registro de pedido

'''
detallePedido = []


def registro(pedidos):

    nombreApellido = input('Ingrese su nombre y apellido: ')
    
    while not " " in nombreApellido:
        print('Porfavor ingresa nombre y apellido')
        nombreApellido = input('Ingrese su nombre y apellido: ')
    direccion = input('Ingresa la direccion: ')

    sector = input('ingrese sector a realizar la entrega(Norte, Centro o Sur)').lower()
    while not sector in sectores:
        print('Ingresa un sector de los anteriormente mencionados')
        sector = input('ingrese sector a realizar la entrega(Norte, Centro o Sur)').lower()

    while True:
        try:
            pequeño = int(input('Ingrese cantidad de paquetes pequeños: '))
            
            mediano = int(input('Ingrese cantidad de paquetes medianos: '))

            grande = int(input('Ingrese cantidad de paquetes grandes: '))


            detallePedido.append('Pequeño: ')
            detallePedido.append(pequeño)

            detallePedido.append('Mediano: ')
            detallePedido.append(mediano)

            detallePedido.append('Grande: ')
            detallePedido.append(grande)
            
            
            break
        except:
            print('Recuerda ingresar numeros.. \n Vuelve a llenar los datos')

    pedidos.append({
        'Cliente' : nombreApellido,
        'Direccion': direccion,
        'Sector' : sector,
        'Detalle': detallePedido
    })

'''
Listar los pedidos

'''

def lista(pedidos):
    for pedido in pedidos:
        print(pedido)


'''

imprimir hoja de ruta

'''

sectorImprimir = []

def imprimir(pedidos):
    sectorSeleccionado = input('Ingresa sector a imprimir (Norte, Centro  o Sur): ').lower()
    while not sectorSeleccionado in sectores:
        print('Ingresa un sector valido')
        sectorSeleccionado = input('Ingresa sector a imprimir (Norte, Centro  o Sur): ').lower()

    for pedido in pedidos:
        if pedido['Sector'] == sectorSeleccionado:
            sectorImprimir.append(pedido)
    '''
    Supongamos que aqui cree el archivo .

    Aqui escribo el archivo con lo que esta dentro de sectorImprimir

    El archivo se creo satisfactoriamente y magicamente usted lo puede ver

    '''
        