lista=[]
ingreso = 1
modificar = 2
eliminar = 3
eliminar_l = 4
buscar = 5
mostrar = 6
salir = 0
indice = 0
x = -1

while x != 0:
    print("(1) Ingresar un elemento a la lista")
    print("(2) Modificar un elemento de la lista")
    print("(3) Eliminar un elemento de la lista según el índice")
    print("(4) Eliminar el último elemento de la lista")
    print("(5) Buscar un elemento de la lista")
    print("(6) Mostrar todos los elementos de la lista")
    print("(0) Salir")
    x = int(input("Eliga una opcion: "))

    if x < 0 and x < 7:
        
        if x == 1:
            while ingreso != "":
                ingreso = input("Ingrese el elemento (presione enter para salir): ")
                lista.append(ingreso)

        if x == 2:
            modificar = input("Ingrese el elemento que desea modificar: ")
            lista.remove(modificar)
            modificar = input("Ingrese el nuevo elemento: ")
            lista.append(modificar)

        if x == 3:
            eliminar = int(input("Ingrese el indice del elemento a elminiar: "))
            lista.pop(eliminar)

        if x == 4:
            lista.pop(-1)

        if x == 5:
            buscar = input("Ingrese el elemento que busca: ")
            indice = lista.index(buscar)
            print ("El elemento ", buscar," esta en el indice", indice)

        if x == 6:
            print(lista)
    else:
        print("Opcion no valida")