def sumarGolosinas(golosinasPedidas):
    
    suma = 0
    
    for golosina in golosinasPedidas:
        
        suma += golosina[2]
        
    return suma
def mostrarGolosinasPedidas(golosinasPedidas):
    
    print("\nGOLOSINAS PEDIDAS")
    for pedidas in golosinasPedidas:
        print(f"ID: {pedidas[0]} - {pedidas[1]} - (Pedido: {pedidas[2]})")
        
def incrementarStock(golosinas,cantidad,codigo):
    
    golosinas[codigo-1][2] += cantidad
    print(f"Usted ingresó {cantidad} {golosinas[codigo-1][1]}. Ahora hay {golosinas[codigo-1][2]} unidades.")
        
    return golosinas  
def rellenarGolosinas(golosinas):
    
    codigo = int(input("\nIngrese el código de la golosina\n"))
    while codigo < 1 or codigo > len(golosinas):
        codigo = int(input("\nCódigo, no válido, por favor ingrese un numero de la lista\n"))
                    
    cantidad = int(input("\nIngrese la cantidad que desea recargar\n"))
    while cantidad <= 0:
        cantidad = int(input("\nLa cantidad debe ser mayor a 0. Intente nuevamente\n"))
                    
    if golosinas[codigo-1][0] == codigo:
        incrementarStock(golosinas,cantidad,codigo)
        return

    return golosinas
def solicitarClave(clavesTecnico):
    admin = str(input("\nPrimer clave:\n"))
    if admin == str(clavesTecnico[0]):
        
        cccddd = str(input("\nSegunda clave:\n"))
        if cccddd == str(clavesTecnico[1]):
            
            anio = int(input("\nTercer clave:\n"))
            if anio == int(clavesTecnico[2]):
                
                return True
            
            else:
                print("No tiene permiso para ejecutar la funcion de recarga")          
                return False
        else:
            print("No tiene permiso para ejecutar la funcion de recarga")          
            return False
    else:
        print("No tiene permiso para ejecutar la funcion de recarga")          
        return False

def mostrarGolosinas(golosinas):
    
    print("\nGOLOSINAS")
    for golosina in golosinas:
        print(f"ID: {golosina[0]} - {golosina[1]} - (Stock: {golosina[2]})")

def cargarGolosinaPedida(golosinasPedidas,codigo,nombreGolosina,cantidad):
    
    for pedidas in golosinasPedidas:
        if pedidas[0] == codigo:  
            pedidas[2] += cantidad  
            break
    else:
        golosinasPedidas.append([codigo, nombreGolosina, cantidad])
            
    return golosinasPedidas
def decrementarStock(golosinas,cantidad,codigo):
            
    golosinas[codigo-1][2] -= cantidad
    print(f"Usted solicitó {cantidad} {golosinas[codigo-1][1]}. Ahora quedan {golosinas[codigo-1][2]} unidades.")
        
    return golosinas  
def pedirGolosina(golosinas,empleados,golosinasPedidas):
    
    legajo = int(input("\nIngrese su numero de legajo\n"))
    
    if legajo in empleados:
        
        while True:
            
            try:
                codigo = int(input("\nIngrese el código de la golosina\n"))
                while codigo < 1 or codigo > len(golosinas):
                    codigo = int(input("\nCódigo, no válido, por favor ingrese un numero de la lista\n"))
                    
                cantidad = int(input("\nIngrese la cantidad que desea llevar\n"))
                   
                for golosina in golosinas:

                    if golosinas[codigo-1][0] == codigo:
                        if golosinas[codigo-1][2] >= cantidad:
                            decrementarStock(golosinas,cantidad,codigo)
                            cargarGolosinaPedida(golosinasPedidas,golosinas[codigo-1][0], golosinas[codigo-1][1],cantidad)
                            return
                        else:
                            opcion = int(input(f"Lo sentimos la golosina {golosinas[codigo-1][1]} no se encuentra disponible,\nseleccione:\n1: Otra golosina\n2: Salir si no desea otra golosina\n"))
                        
                            if opcion == 2:
                                return
                        break
                    
            except ValueError:
            
                print("Por favor, ingrese un numero valido")   
    else:
        print("Usted no es un empleado de la empresa")

    return golosinas,golosinasPedidas     

def menu(golosinas,empleados,clavesTecnico,golosinasPedidas):
    
    opcion = ""
    while opcion != 4:
        opcion = int(input("\nIngrese una opcion\n1:Pedir golosina\n2:Mostrar golosinas\n3:Rellenar golosinas\n4:Apagar maquina\nOpcion: "))

        if opcion == 1:
            pedirGolosina(golosinas,empleados,golosinasPedidas)
        
        if opcion == 2:
            mostrarGolosinas(golosinas)
            
        if opcion == 3:
            if solicitarClave(clavesTecnico):
                rellenarGolosinas(golosinas)
            
        if opcion == 4:
            mostrarGolosinasPedidas(golosinasPedidas)
            sumaGolosinas = sumarGolosinas(golosinasPedidas)
            
            print(f"La cantidad total de golosinas pedidas es de {sumaGolosinas} unidades")
            
            break
    
golosinas = [[1, "Kit Kat", 20],
            [ 2, "Chicles", 50],
            [ 3, "Caramelos", 50],
            [ 4, "Huevo kinder", 10],
            [ 5, "Chetoos", 10],
            [ 6, "Twix", 10],
            [ 7, "M$M'S", 10],
            [ 8, "Papas Lays", 2],
            [ 9, "Milkbar", 10],
            [ 10, "Alfajor Tofi", 15],
            [ 11, "Lata Coca", 20],
            [ 12, "Chitos", 10]]

empleados = {
    1100: "José Alonso",
    1200: "Federico Pacheco",
    1300: "Nelson Pereira",
    1400: "Osvaldo Tejada",
    1500: "Gastón Garcia"
}

clavesTecnico = ("admin","CCCDDD",2020)

golosinasPedidas = []
    

menu(golosinas,empleados,clavesTecnico,golosinasPedidas)