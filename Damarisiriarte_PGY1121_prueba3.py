import random
import re

vehiculos=[]

def verficar_patente(patente):
    patron=r'^[A-Z]{4}/d{2}$'
    return re.match(patron, patente) is not None
def generar_valor_aleatorio():
    return random.randint(1500, 3500)
def buscar_vehiculo(patente):
    for vehiculo in vehiculos:
        if vehiculo['patente'] == patente:
            return vehiculo 
        return None
    def imprimir_certificado(patente):
        vehiculo= buscar_vehiculo(patente)
        if vehiculo:
           print("--------Certificados de Emisión de contaminantes--------")
           print("Nombre del certificado: ",vehiculo['nombre_certificado'])
           print("Patente del vehiculo: ", vehiculo['patente'])
           print("Datos del dueño: ")
           print("Nombre:   ",vehiculo['nombre_dueno'])
           print("Tipo:", vehiculo['tipo'])
           print("Marca: ", vehiculo['marca'])
           print("Precio:  $", vehiculo['precio'])
           print("Anotaciones vigentes y multas:  ")
           for multa in vehiculo['multas']:
               print("Fecha:  ", multa['fecha'])
               print("Monto:  ", multa['monto'])
        else:
            print("No se encontro un vehiculo con la patente especificada!")
    while True:
        print("Bienvenido a la Automotora 'Auto Seguro' ")        
        print("1.Grabar vehiculo")
        print("2.Buscar vehiculo por patente")
        print("3.Imprimir certificado de emision de contaminantes")
        print("4.Salir.")
        opc=input("Selecciona una opción:  ")

        if opc == "1":
            print("Ingresa los datos del vehiculo:  ")
            tipo=input("Tipo:  ")
            patente=input("Patente:  ")
            marca=input("Marca:  ")
            precio=float(input("Precio:  "))
            multas=[]
            while True:
                opc_multa = input("Agregar multa?S/N:  ")
                if opc_multa.lower() == 'n':
                    break
                monto= generar_valor_aleatorio()
                fecha= input("Fecha de multa:  ")
                multa={'monto': monto, 'fecha': fecha}
                multas.append(multa)
            fecha_registro=input("Fecha de registro:  ") 
            nombre_dueno=input("Nombre del dueño:  ")
            if verficar_patente(patente) and len(patente)== 6 and 2 <= len(marca) <= 15 and precio > 5000000:
                vehiculo = {
                    'tipo': tipo,
                    'patente': patente,
                    'marca': marca,
                    'precio': precio,
                    'multas': multas,
                    'fecha_registro': fecha_registro,
                    'nombre_dueno': nombre_dueno,
                    'nombre_certificado': imprimir_certificado +patente}
                vehiculos.append(vehiculo)
                print("Vehiculo grabado exitosamente!!!")
            else:
                print("Error!! los datos ingresados no son validos!. Verifica que la patente tenga el formato correcto (4 letras seguidas de 2 numeros)")

        elif opc == "2":
            patente = input("ingresa la patente del vehiculo a buscar:  ") 
            vehiculo= buscar_vehiculo(patente)
            if vehiculo:
                print("vehiculo encontrado!")
                print("Tipo: ", vehiculo['tipo'])
                print("Marca:  ",vehiculo['marca'])
                print("Prrrrecio: $$", vehiculo['precio'])
            else:
                print("no se encontro vehiculo con esa patente!!!")

        elif opc == "3":
            patente= input("ingrese la patente para imprimir certificado:  ")
            imprimir_certificado(patente)

        elif opc == "4":
            print("datos guardados")
            break
        else:
            print("opción invalida!!!. Selecciona otra opción.")



        

                   
