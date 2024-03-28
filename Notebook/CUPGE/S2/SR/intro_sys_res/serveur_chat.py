    serveursocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    serveursocket.bind(('localhost',8080))
    while True:
        requete,(IP_client, Port_client) = clientsocket.recvfrom(1024)
        clientsocket.sendto("Bien reçu !",(IP_client, Port_client))
