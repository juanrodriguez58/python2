import urllib.request
from re import findall

def getUrl(texto):
# req = 'http://www.freecsstemplates.org/r/'
    try:
        req = texto
        response = urllib.request.urlopen(req)
        server = str(response.geturl())
        print(server)
        c = len(findall('(?=/)',server))
        if c > 2:
            server = server.split(sep="/", maxsplit=-3)[2]
        print("Server: ",  server)
        t = server, str(response.read())
        return(t)
    except urllib.error.HTTPError:
    	print("Error en la llamada")
