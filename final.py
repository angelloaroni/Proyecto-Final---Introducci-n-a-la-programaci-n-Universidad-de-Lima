import random


def Menu():
    serviciosSet = set()
    listaServicios = []
    
    while True: 
        print("---SISTEMA DE ADMINISTRACIÓN DE SERVICIOS---")

        print("1.- Ingresar un tipo de servicio")
        print("2.- Registrar una venta")
        print("3.- Modificar una venta a través del número de venta")
        print("4.- Ordenar ventas por total")
        print("5.- Buscar una venta por numero de venta")	
        print("6.- Mostrar venta con total mas alto")
        print("7.- Almacenar información en un archivo físico")
        print("0.-INTRODUCE 0 PARA SALIR DEL PROGRAMA") 

        accion = int(input("Introduce el número de la acción a realizar: "))
        while accion > 7 or accion < -1:
            print("Introduce una acción valida")
            accion = int(input("Introduce el número de la acción a realizar: "))
        
        if accion == 0:
            print("Gracias por hacer uso del sistema")
            break
        elif accion == 1:

            añadir = True
            while añadir != "no" and len(serviciosSet) < 3:
            
                servicio, serviciosSet = IngresarServicio(serviciosSet)
                listaServicios.append(servicio)
                
                if len(serviciosSet) == 3:
                    break
                añadir = input("Desea anadir otro servicio (si/no): ")

            print("---------------------------------------------\nHa alcanzado la cantidad máxima de servicios posibles a registrar\n---------------------------------------------")
  
        elif accion == 2:
            pass
        elif accion == 3:
            pass
def generarInformacion(servicioIngresado):
        
        servicio = {

        }

        codigoServico = random.randint(30000, 80000)
        while codigoServico % 5 != 0:
            codigoServico = random.randint(30000, 80000)
        

        #no entiendo como se supone que se sepa si hay beneficio o no, lo calculo de manera aleatorio pero facilmente puede adaptarse a un input
        beneficio = random.choice([True, False])
        if servicioIngresado.lower() == "viaje nacional":
            descripcion = "El servicio de Viaje nacional, le permite a usted, llegar a cualquier departamento del país, para poder conocer las bellezas de Perú."
            precio = random.randint(150, 350)
            while precio % 2 != 0:
                precio = random.randint(150, 350)

        elif servicioIngresado.lower() == "viaje internacional":
            descripcion = "El servicio de Viaje internacional, le permite a usted, llegar a todos los rincones del mundo, para poder conocer las bellezas del planeta"
            precio = random.randint(380, 750)
            while precio % 3 != 0:
                precio = random.randint(380, 750)

        else:
            descripcion = "El servicio de Paquete turístico le permite viajar sin tener que preocuparse por el alojamiento, la comida o el transporte, puesto que TODO se incluye en un solo pago"
            precio = random.randint(390, 855)
            while precio % 2 ==  0:
                precio = random.randint(390, 855)

        servicio["Codigo de servicio"] = codigoServico
        servicio["Descripción"] = descripcion
        servicio["Beneficio"] = beneficio
        servicio["Precio"] = precio

        return servicio
    
def IngresarServicio(serviciosSet):
         
        print("Ingrese que tipo de serviio desea registrar (Viaje nacional, Viaje internacional, Paquete turístico)")

        servicioIngresado = input("Nombre del servicio: ")
        while servicioIngresado.lower() in serviciosSet:
            print("Este servicio ya ha sido ingresado con anterioridad, por favor, eliga otro")
            servicioIngresado = input("Nombre del servicio: ")
        
        while servicioIngresado.lower() != "viaje nacional" and servicioIngresado.lower() != "viaje internacional" and servicioIngresado.lower() != "paquete turistico":
            print("Servicio no valido")
            servicioIngresado = input("Nombre del servicio: ")
        serviciosSet.add(servicioIngresado)

        servicio = generarInformacion(servicioIngresado)
        print(servicio)

        return servicio, serviciosSet



    
    




    

if __name__ == "__main__":
    
    Menu()
