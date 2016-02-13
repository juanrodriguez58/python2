def arregla(cadena, servidor):
    tipo = "link"
    dir = cadena
    if cadena.startswith("http://") or cadena.startswith("https://"):
        tipo = validafin(cadena)
    else:
        dir = arreglaIni(cadena,servidor)
        tipo = validafin(cadena)
    t = dir,  tipo
    return t
    
def validafin(cadena2):
    var = "link"
    if cadena2.endswith(('.jpg"','.jpeg"','.gif"','.JPG"','.png"')):
        var="img"
    elif cadena2.endswith(('.mp4"','.mpeg"','.avi"')):
        var="video"
    elif cadena2.endswith(('.com"','.org"','.es"','/','.eu"')):
        var="link"
    else:
        var="linx"
    return var
    
def arreglaIni(cad,  serv):
    salida = cad
    
    if cad.startswith("src"):
        cad = cad[4:]
    elif cad.startswith("href"):
        cad = cad[5:]
    
    if cad.startswith('"/'):
        salida = serv + cad
    elif cad.startswith("www."):
        salida = 'http://' + cad
    else:
        salida = cad
    
    if salida.startswith('"http://'):
        return salida
    elif salida.startswith('"https://'):
        return salida
    else:
        print("No va -->",  salida)
        return "0"
    
        
