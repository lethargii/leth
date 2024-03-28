import socket
import doctest

ex_requete_http1="GET /page1.html HTTP/1.1\r\nHost: localhost\r\nAccept-Language: fr-FR,en;q=0.3\r\nUser-Agent: Mozilla/5.0 Firefox/98.0\r\n\r\n"

ex_requete_http2="GET /pages/index.html HTTP/1.1\r\nHost: localhost\r\nAccept-Language: fr\r\n\r\n"
ex_requete_http3="GET /autres_pages/toto.html HTTP/1.1\r\nHost: localhost\r\n\r\n"

def decode_requete_http(requete) :
    """
    >>> a,b = decode_requete_http(ex_requete_http1)
    >>> a == "/page1.html"
    True
    >>> len(b)
    3
    >>> b["Host"] == "localhost"
    True
    >>> b["Accept-Language"] == "fr-FR,en;q=0.3"
    True
    >>> b["User-Agent"] == "Mozilla/5.0 Firefox/98.0"
    True
    """
    requete_decode = requete.split("\r\n")
    page = requete_decode[0].split(" ")[1]
    options = {}
    for i in range(1, len(requete_decode)-2):
        option = requete_decode[i].split(": ")
        options[option[0]]=option[1]
    return page,options

def get_reponse(url_page) :
    """
    >>> a = get_reponse("pages_serveur/fr/pages/index.html")
    >>> a == "HTTP/1.0 200 OK\\r\\nContent-Type:text/html\\r\\nContent-Length:74\\r\\n\\r\\n<!DOCTYPE html>\\n<html>\\n<body>\\n<h1>Voici index.html !</h1>\\n</body>\\n</html>\\r\\n"
    True
    >>> b = get_reponse("page_non_existante")
    >>> b == "HTTP/1.0 404 NotFound\\r\\nContent-Type:text/html\\r\\nContent-Length:173\\r\\n\\r\\n<!DOCTYPE html>\\n<html>\\n<head><title>404 Not Found</title></head><body>\\n<h1>Page non trouvée !!</h1>\\n<p>L'URL demandée n'a pas été trouvée sur ce serveur.</p></body>\\n</html>\\r\\n"
    True
    """
    try:
        fichier = open(url_page,"r")
        data = fichier.read()
        reponse = f"HTTP/1.0 200 OK\r\nContent-Type:text/html\r\nContent-Length:{len(data)+1}\r\n\r\n"+data+"\r\n"
    except Exception:
        fichier = open("pages_serveur/page404.html","r")
        data = fichier.read()
        reponse = f"HTTP/1.0 404 NotFound\r\nContent-Type:text/html\r\nContent-Length:{len(data)+1}\r\n\r\n"+data+"\r\n"
    return reponse

def traite_requete(requete) :
    """
    >>> traite_requete(ex_requete_http2) == get_reponse("pages_serveur/fr/pages/index.html")
    True
    >>> traite_requete(ex_requete_http3) == get_reponse("pages_serveur/en/autres_pages/toto.html")
    True
    """
    page,options = decode_requete_http(requete)
    if 'Accept-Language' in options and options['Accept-Language'][0:2]=='fr':
        url_page = 'pages_serveur/fr'+page
    else:
        url_page = 'pages_serveur/en'+page
    return get_reponse(url_page)

if __name__ == "__main__" :
    doctest.testmod()
    serveursocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    serveursocket.bind(('localhost',8080))
    while True:
        serveursocket.listen()
        clientsocket, (IP_client, Port_client) = serveursocket.accept()
        requete = clientsocket.recv(65565)
        print(requete.decode("utf-8"))
        reponse = traite_requete(requete.decode("utf-8"))
        clientsocket.send(reponse.encode("utf-8"))
        clientsocket.close()
