# Opciones
# 'e' --> recupera sólo enlaces + estadísticas
# 'ei' --> recupera sólo enlaces + imagenes
# 'ea' --> recupera todo sin estadisticas
# 'eea' --> recupera todo con estadisticas

import beautifuler
import web
import cadena
import sqlfile

# Araña

def tejer(inicio, profundidad, nivel, opcion):

# Crear tabla de control del ciclo. Borramos primero, por si ya existe.

    print(sqlfile.borraTabla())
    print(sqlfile.creaTabla())

# Tabla cicle: Direccion, tipo de enlace, indicador pendiente-visto (1,0), contador llamadas

# Inicializa las listas
    listaEnlaces = []
    listaPendientes = []

    listaPendientes.append(inicio)
    listaEnlaces.append(inicio)

# Operativa por cada nivel
    
    n = 0
    while n < profundidad: 

        print("Cargo lista pendientes")
        listaPendientes = sqlfile.consultaPendientes()
        
        for reg in listaPendientes:
            print("Busco el registro en la web")
            t1 = web.getUrl(reg)
            serv = t1[0]
            lineas = t1[1]
            print("Obtengo los enlaces")
            for linea in lineas:
                t2 = beautifuler.arregla(linea, serv)
                dire = t2[0]
                tipo = t2[1]
                print("Pongo bonito el enlace")
                print("saco el tipo del enlace")
                if dire != '0':
                    niv = cadena.contarCaracter(dire, '/')
                    print("Busco si existe el enlace en la lista")
                    print("Si existe actualizo contador, si no inserto")
                    num = sqlfile.consultaCount2(dire)
                    if num > 0:
                        num = num + 1
                        sqlfile.actualizaCount2(dire, num)
                    else:
                        if tipo == 'link':
                            if niv <= nivel:
                                sqlfile.insertaCount(dire, tipo,1,1)
                            else:
                                sqlfile.insertaCount(dire, tipo,0,1)
                                print("Inserto en la lista de enlaces pendientes")
                                print("Si el tipo del enlace es enlace y el nivel menor que el nivel")
                                print(".. entonces guardalo para leer")
                        else:
                            sqlfile.insertaCount(dire, tipo,0,1)
            print("Marco como leido el registro en la lista de pendientes con un caracter especial al final")
            sqlfile.actualizaCount1(reg, 0)
            
# bajo en una unidad la profundidad

        n = n + 1
        esc = input("Finalizar (S/N) \n")
        if esc == 'S':
            break
            
        
# Salidas despues de finalizar
        
    print(sqlfile.consultaTodos())

