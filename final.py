import random

def Menu(serviciosSet, listaServicios, listaVentas):
    
    
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
            print("---Gracias por hacer uso del sistema---")
            break
        elif accion == 1:
            if len(serviciosSet) == 3:
                print("---------------------------------------------\nHa alcanzado la cantidad máxima de servicios posibles a registrar\n---------------------------------------------")

            añadir = True
            while añadir != "no" and len(serviciosSet) < 3:
            
                servicio, serviciosSet = IngresarServicio(serviciosSet)
                listaServicios.append(servicio)           
                if len(serviciosSet) == 3:
                    break
                añadir = input("Desea anadir otro servicio (si/no): ")

        elif accion == 2:

            listaVentas = RegistrarVenta(serviciosSet, listaServicios, listaVentas)
            print(listaVentas)

        elif accion == 3:
            listaVentas = ModificarVenta(listaVentas)
        elif accion == 4:
            listaVentas = OrdenarVentas(listaVentas)
        elif accion == 5:
            MostrarDatosDeVenta(listaVentas)
        elif accion == 6:
            TotalMasAlto(listaVentas)
        elif accion == 7:
            InformaciónEnArchivo(listaVentas)

def quicksort(listaVentas):
    #debe ordenarse el codigo de venta porque en caso de ejecutase la funcion 4 anteriormente
    #no va a ejecutar bien el codigo, la lista no estara ordenada
    if len(listaVentas) <= 1:
        return listaVentas
    else:
        tempPivot = listaVentas[0]
        pivot = listaVentas[0]["Codigo de venta"]
        menores = []
        mayores = []
        for i in range(1, len(listaVentas)):
            if listaVentas[i]["Codigo de venta"] > pivot:
                mayores.append(listaVentas[i])
            else:
                menores.append(listaVentas[i])
            
            menores = quicksort(menores)
            mayores = quicksort(mayores)
        
        return menores + [tempPivot] + mayores
        
def busquedaBinaria(listaVentas):
    #debe retornar un index
    print(listaVentas)
    listaCodigos = quicksort(listaVentas)
    print("/**/*/*/*/*/*/*/")
    print(listaCodigos)
    # for venta in listaVentas:
    #     listaCodigos.append(venta["Codigo de venta"])

    
    
    izq = 0
    derecha = len(listaCodigos) - 1
    buscado = int(input("Introduce el numero de venta de la venta que quiere modificar: "))
    while izq <= derecha:
        medio = (izq + derecha) // 2
        if listaCodigos[medio]["Codigo de venta"] == buscado:
            return medio, listaVentas 
        elif listaCodigos[medio]["Codigo de venta"] < buscado:
            izq = medio + 1
        else:
            derecha = medio - 1
    return -1

def OrdenamientoBrubuja(listaVentas):

    if len(listaVentas) == 0:
        print("No existen ventas registradas en el sistemas")
    elif len(listaVentas) == 1:
        return listaVentas
    
    #print(sorted(listaVentas, key=lambda k: k["Total de la venta"], reverse=True))
    for i in range(len(listaVentas)-1):
        for j in range(len(listaVentas)-i-1):
            if listaVentas[j]["Total de la venta"] < listaVentas[j+1]["Total de la venta"]:
                aux = listaVentas[j]
                listaVentas[j] = listaVentas[j+1]
                listaVentas[j+1] = aux

    return listaVentas
def generarInformacion(servicioIngresado):
        
        servicio = {

        }

        codigoServico = random.randint(30000, 80000)
        while codigoServico % 5 != 0:
            codigoServico = random.randint(30000, 80000)
        

        #no entiendo como se supone que se sepa si hay beneficio o no, lo calculo de manera aleatorio pero facilmente puede adaptarse a un input
        beneficio = random.choice([True, False])

        #solo cambia la descripcion y precio entre los 3 productos, no tocar nada de aqui
        #las variables que no aparezcan aqui son "constatntes" dentro de la funcion    
        beneficio = "No"
        #no entiendo como se supone que se sepa si hay beneficio o no, lo calculo de manera aleatorio pero facilmente puede adaptarse a un input
        # beneficio = random.choice([True, False])
        tieneBeneficio = input("¿Tiene beneficio tributario?: (ingrese 'si' para indicar que cuenta con uno, cualquier otro valor para indicar que no): ")
        if tieneBeneficio.lower() == "si":
            beneficio = "Si"
        if servicioIngresado.lower() == "viaje nacional":
            descripcion = "El servicio de Viaje nacional, le permite a usted, llegar a cualquier departamento del país, para poder conocer las bellezas de Perú."
            precio = random.randint(150, 350)
            while precio % 2 != 0:
                precio = random.randint(150, 350)
            tipoServicio = "Viaje nacional"
            

        elif servicioIngresado.lower() == "viaje internacional":
            descripcion = "El servicio de Viaje internacional, le permite a usted, llegar a todos los rincones del mundo, para poder conocer las bellezas del planeta"
            precio = random.randint(380, 750)
            while precio % 3 != 0:
                precio = random.randint(380, 750)
            tipoServicio = "Viaje internacional"

        else:
            descripcion = "El servicio de Paquete turístico le permite viajar sin tener que preocuparse por el alojamiento, la comida o el transporte, puesto que TODO se incluye en un solo pago"
            precio = random.randint(390, 855)
            while precio % 2 ==  0:
                precio = random.randint(390, 855)
            tipoServicio = "Paquete turístico"
            
        servicio["Servicio"] = tipoServicio
        servicio["Codigo de servicio"] = codigoServico
        servicio["Descripción"] = descripcion
        servicio["Beneficio"] = beneficio
        servicio["Precio"] = precio
    
        #servicion es UN SOLO diccionario, fuera de esta funcion se añade a la lista
        return servicio




def IngresarServicio(serviciosSet):
         
        print("Ingrese que tipo de serviio desea registrar (Viaje nacional, Viaje internacional, Paquete turístico)")
    
        #no tocar nada en esta funcion
        servicioIngresado = input("Nombre del servicio: ")
        while servicioIngresado.lower() in serviciosSet:
            print("Este servicio ya ha sido ingresado con anterioridad, por favor, eliga otro")
            servicioIngresado = input("Nombre del servicio: ")
        
        while servicioIngresado.lower() != "viaje nacional" and servicioIngresado.lower() != "viaje internacional" and servicioIngresado.lower() != "paquete turistico":
            print("Servicio no valido")
            servicioIngresado = input("Nombre del servicio: ")
        serviciosSet.add(servicioIngresado)
    
        #no tocar
        servicio = generarInformacion(servicioIngresado)
        print(servicio)

        return servicio, serviciosSet


def RegistrarVenta(servicioSet, listaServicios, listaVentas):
    #este codigo es correlativo, la funcion venta aun no esta hecha, sospecho que va a tener que estar
    #fuera de esta funcion, y su numero tendra que trabajarse desde la parte de Menu()
    #tener en cuenta que para el sistema de ventas necesito diccionario con las ventas, que tenga numeroVenta correlativo, aca dice precio sin IGV, luego
    # precio teniendo en cuenta beneficio tributario (???), trabajarlo si hay beneficio tributario = NO IGV, cantidadVenta > 1 y < 10, totalVenta = precio*cantidad
    # entiendo ventas de un solo producto, tratar de que el codigo sea adaptable en caso de poder venderse mas por mala explicaicon del profe
    

    #la cantidad de venta debe ser
    ventas = [] 
    
    
    
    if len(listaServicios) == 0:
        print("No hay servicios registrados, por favor, primero ingrese los servicios antes de empezar con las ventas")
        return listaVentas
    añadir = True
    while añadir != "no":
        productoVenta = (input(f"Introduce el nombre del prodcto que deseas vender: "))

        while  productoVenta not in servicioSet:
            print("El producto que quiere vendeer no se encuentra registrado, ingrese otro")
            productoVenta = input("Introduce el nombre del prodcto que deseas vender: ")

        #la cantidad de venta no debe ser mayor a 10 ni menor a 0
    
        cantidadVenta = int(input(f"Ingrese la cantidad de {productoVenta} que se va a vender: "))
        while cantidadVenta < 0 or cantidadVenta > 10:
            print("La cantida de venta no debe exceder las 10 unidades por venta, ni ser menor a 0")
            cantidadVenta = int(input(f"Ingrese la cantidad de {productoVenta} que se va a vender: "))
        
        for diccionario in listaServicios:
            diccionarioVenta = {
        
        }
            if diccionario["Servicio"].lower() == productoVenta.lower():
                preciosinIGV = diccionario["Precio"]
                precioconIGV = preciosinIGV + 18/100 * preciosinIGV
                totalVenta = precioconIGV * cantidadVenta
                if diccionario["Beneficio"].lower() == "si":
                    beneficio = "Tiene beneficio"
                else:
                    beneficio = "No tiene beneficio"

                #si no existe la venta, se inicia en 10k
                if len(listaVentas) == 0:
                    numeroVenta = 1
                else:
                    #un poco extraño, no encontre otra forma de hacerlo, se busca la ultima venta registrada y se le suma 1 al codigo de esa venta
                    #tuve problemas con la iniciacion de la variable xd, solo quedo esto
                    numeroVenta = listaVentas[-1]["Codigo de venta"] + 1
            

                #un poco largo
                diccionarioVenta["Servicio"] = diccionario["Servicio"]
                diccionarioVenta["Beneficio"] = beneficio
                diccionarioVenta["Precio de venta"] = precioconIGV
                diccionarioVenta["Unidades vendidas"] = cantidadVenta
                diccionarioVenta["Total de la venta"] = round(totalVenta, 3)
                diccionarioVenta["Codigo de venta"] = numeroVenta
                listaVentas.append(diccionarioVenta)

        añadir = input("¿Desea añadir otra venta? (si/no): ") 
    return listaVentas

def ModificarVenta(listaVentas):
    if len(listaVentas) == 0:
        print("No existen ventas registradas aún")
        return listaVentas
    
    index, listaVentas = busquedaBinaria(listaVentas)
    print(index)
    print("*******")
    print(listaVentas[index])
    if index == -1:
        print("No se encontró el número de venta buscado")
        return listaVentas
    else:
        nuevaCantidadVenta = int(input("Ingrese la nueva cantidad de la venta: "))
        while nuevaCantidadVenta < 0 or nuevaCantidadVenta > 10:
            nuevaCantidadVenta = int(input("La cantidad debe estar entre 0 y 10. Ingrese nuevamente: "))
        
        listaVentas[index]["Unidades vendidas"] = nuevaCantidadVenta
        listaVentas[index]["Total de la venta"] = listaVentas[index]["Precio de venta"] * nuevaCantidadVenta

        print("Venta modificada correctamente:")
        print(listaVentas[index])
        return listaVentas


            
def OrdenarVentas(listaVentas):

    listaVentas = OrdenamientoBrubuja(listaVentas)
    #poner un print
    print("-----------------------------------")
    print("Se ha ordenado con exito la lista")
    print("-----------------------------------")

    return listaVentas

def MostrarDatosDeVenta(listaVentas):
    codigos = []

    for venta in listaVentas:
        codigos.append(venta["Codigo de venta"])

    if len(codigos) == 0:
        print("No existen ventas registradas aún")
        return listaVentas

    numeroVentaBuscado = int(input("Ingrese el numero de venta de la venta de la que desea ver la información: "))
    while numeroVentaBuscado not in codigos or numeroVentaBuscado <= 0:
        print("No existe una venta registrada con ese código, por favor, ingrese otro")
        numeroVentaBuscado = int(input("Ingrese el codigo de la venta que desea modificar: "))

    #piden usar busqueda secuencial
    for venta in range(0, len(listaVentas)):
        if (listaVentas[venta]["Codigo de venta"] == numeroVentaBuscado):
            print("----------INFORMACIÓN DE LA VENTA----------\n")

            print(f"Servicio vendido: {listaVentas[venta]['Servicio']}")
            print(f"¿Tiene beneficio?: {listaVentas[venta]['Beneficio']}")
            print(f"Precio de la venta (por unidad): {listaVentas[venta]['Precio de venta']}")
            print(f"Cantidad de unidades vendidas: {listaVentas[venta]['Unidades vendidas']}")
            print(f"Monto total de la venta: {listaVentas[venta]['Total de la venta']}")
            print(f"Numero de venta: {listaVentas[venta]['Codigo de venta']}\n")
            break

def TotalMasAlto(listaVentas):
    if len(listaVentas) == 0:
        print("No existen ventas registradas en el sistemas")
        return listaVentas
    listaVentas = OrdenamientoBrubuja(listaVentas)
    print(f"\n---INFORMACIÓN DE LA VENTA CON EL TOTAL MAS ALTO---\n")

    print(f"Servicio vendido: {listaVentas[0]['Servicio']}")
    print(f"¿Tiene beneficio?: {listaVentas[0]['Beneficio']}")
    print(f"Precio de la venta (por unidad): {listaVentas[0]['Precio de venta']}")
    print(f"Cantidad de unidades vendidas: {listaVentas[0]['Unidades vendidas']}")
    print(f"Monto total de la venta: {listaVentas[0]['Total de la venta']}")
    print(f"Numero de venta: {listaVentas[0]['Codigo de venta']}\n")

def InformaciónEnArchivo(listaVentas):
    if len(listaVentas) == 0:
        print("No hay información que se puede almacenar dentro de un archivo, por favor, primero ingrese una venta")
        return listaVentas
    #no entiendo que se almacena aca, si la informacion de al ventas (me inclino a pensar esto) o la informacion general de los productos
    #me parece correcto usar os pero supongo que es bueno consdeirar cambiarlo (quizas pc del profe o donde se vaya a exponer no se tenga instalada la libreria)
    # if  not os.path.exists("Ventas.txt"):
    #     with open("Ventas.txt", "w") as archivo:
    #         print("Se ha creado el archivo")

    with open("Ventas.txt", "w", encoding="utf-8") as archivo:
        for venta in listaVentas:

            archivo.writelines(f"Servicio vendido: {venta['Servicio']}\n")
            archivo.writelines(f"¿Tiene beneficio?: {venta['Beneficio']}\n")
            archivo.writelines(f"Precio de la venta (por unidad): {venta['Precio de venta']}\n")
            archivo.writelines(f"Cantidad de unidades vendidas: {venta['Unidades vendidas']}\n")
            archivo.writelines(f"Monto total de la venta: {venta['Total de la venta']}\n")
            archivo.writelines(f"Numero de venta: {venta['Codigo de venta']}\n\n")

    archivo.close()

        

    


if __name__ == "__main__":

    serviciosSet = set()
    listaServicios = []
    listaVentas = []
    
    Menu(serviciosSet, listaServicios, listaVentas)




#posibles errores, deberia verificar si es que pueden salir precios con decimales, algunos me estan tirando eso en los prints
#existe una posibilidad de mejor en TODAS las opciones de (si/no)
#aun falta cambiar la funcion de modificar venta, pero en general, no parece demasiado complicado, nada mas hay que añadir algunas algoritmos


#posibles errores, deberia verificar si es que pueden salir precios con decimales, algunos me estan tirando eso en los prints
#existe una posibilidad de mejor en TODAS las opciones de (si/no)
#aun falta cambiar la funcion de modificar venta, pero en general, no parece demasiado complicado, nada mas hay que añadir algunas algoritmos
