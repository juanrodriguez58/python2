
# Araña

def tejer(inicio, nivel, opcion):

# Inicializa las listas
    listaEnlaces = []
    listaImagenes = []
    listaVideo = []
    listaServidores = []
    listaOtros = []
    listaPendientes = []

    listaPendientes.append(inicio)

# Operativa por cada nivel
    while n < nivel: 
        n = 0
        for reg in listaPendientes:
            print("Busco el registro en la web")
            print("Obtengo los enlaces")
            print("Para cada enlace de tipo enlace")
            print("Pongo bonito el enlace")
            print("saco el tipo del enlace")
            print("Busco el enlace en la lista correspondiente")
            print("Si no existe, lo añado")
            print("Si existe, actualizo el contador")
            print("Busco el enlace en la lista de Pendientes")
            print("Si no existe, lo añado")
            print("Marco como leido el registro en la lista de pendientes con un caracter especial al final")
        n = n + 1
        
# Salidas despues de finalizar
        
    print("Guado en BD")
    for enlace in listaEnlaces:
        print(enlace)
    for enlace in listaImagenes:
        print(enlace)
    for enlace in listaVideo:
        print(enlace)
    for enlace in listaServidores:
        print(enlace)
    for enlace in listaOtros:
        print(enlace)

    if opcion = "e":
        return listaEnlaces
    elif opcion = "i":
        return listaImagenes
    elif opcion = "v":
        return listaVideo
    elif opcion = "s"
        return listaServidores
    else:
        return listaOtros

