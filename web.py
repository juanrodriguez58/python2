import urllib.request

def getUrl(texto):
# req = 'http://www.voidspace.org.uk'
    try:
        req = texto
        response = urllib.request.urlopen(req)
        return(str(response.read()))
    except urllib.error.HTTPError as e:
    	print(e.code)
    	print(e.read()) 
