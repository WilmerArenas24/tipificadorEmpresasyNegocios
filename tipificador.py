'''clase para cliente'''
servicioAfectado = ['INTERNET @',
                    'CITOFONIA B',
                    'CLARO VIDEO G',
                    'INTERNET / TELEFONIA J',
                    'TELEVISION / INTERNET K',
                    'TELEFONIA L',
                    'TELEVISION / TELEFONIA M',
                    'TELEVISION / INTERNET / TELEFONIA N',
                    'ELEGIDO FIJO MOVIL O',
                    'TELEVISION T',
                    'PORTAL MI CLARO U',
                    'PBX Y',
                    'CONTROL REMOTO 1']
solictudCliente = [" POR FALLA DE "," SOLICTANDO INFORMACION" ]
estadoDeSolicitud = ['Abierto', 'Escalado', 'Cerrado']

def crearRadicado():
    nombreRegistro = input('Ingrese el nombre del cliente ')
    cedulaRegistro = input('Ingrese la cedula del cliente ')
    nitClienteRegistro = input('Ingrese el NIT ')
    razonSocialRegistro = input('Ingrese la razon social ')
    cuentaRegistro = input('Ingrese la cuenta ')
    cargoRegistro = input('Ingrese el cargo ')
    servicioAfectadoRegistro = servicioAfectado[0]
    solictudClienteRegistro = solictudCliente[0]
    telefonoOrigenRegistro = input('Ingrese el telefono de origen ')
    telefonoClienteRegistro = input('Ingrese el telefono cliente ')
    estadoCMRegistro = input('Ingrese el estado de CM ')
    equipoRegistro = input('Ingrese el equipo ')
    vecinosRegistro = input('Ingrese tres vecinos ')
    nivelesRegistro = input('Ingrese los niveles ')
    aprovisionamientoRegistro = input('Aprovisionamiento ')
    pqrRegistro = input('Ingrese el numero de pqr ')
    marcacionRegistro = input('Ingrese la amrcacion ')
    estadoSolicituRegistro = estadoDeSolicitud[1]

    print(f'Nombre: {nombreRegistro}\n'
          f'Cedula: {cedulaRegistro}\n'
          f'Nit: {nitClienteRegistro}\n'
          f'Razon social: {razonSocialRegistro}\n'
          f'Cuenta: {cuentaRegistro}\n'
          f'Cargo: {cargoRegistro}\n'
          f'Servicio afectado: {servicioAfectadoRegistro}\n'
          f'Solicitud del cliente: {solictudClienteRegistro}\n'
          f'Telefono de origen: {telefonoOrigenRegistro}\n'
          f'Telefono de cliente: {telefonoClienteRegistro}\n'
          f'Estado CM: {estadoCMRegistro}\n'
          f'Equipo: {equipoRegistro}\n'
          f'Vecinos: {vecinosRegistro}\n'
          f'Niveles: {nivelesRegistro}\n'
          f'Aprovisionamiento: {aprovisionamientoRegistro}\n'
          f'PQR: {pqrRegistro}\n'
          f'Marcacion: {marcacionRegistro}\n'
          f'Estado solictud: {estadoSolicituRegistro}\n')

crearRadicado()






