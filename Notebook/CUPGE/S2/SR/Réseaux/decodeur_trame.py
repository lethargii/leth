import struct
import doctest
import socket

ex_udp = b'\x00-\xd9\x9e\x00\x0eR\x8ccoucou'
ex_tcp = b'\x00-\xd7[\x00\x00\x17\x15\x00\x00\x04e\x86\xc6\ndg!By!\xaf\xff&\xfc\x19R\xcc\x18\xac|(coincoin'
ex_icmp = b'\x05\x04g\x90\x1a@\xc9\x01'
ex_ip = b"H\xf7\x00&[\x0cI\r\xe5\x01v5\xea\xd8\xa0\xe5L\xda\x86\x93\x0e\xa0\xed\xe8\x99\xc1G\xc0{P'\xc4cuicui"
ex_eth = b'R\x0c\xc7\x1d\xca578\x1fUk\x98\x08\x00coicoi'

ex_complet1 = b'Q\xf0\xdeG?\xf4\xa0\x18\x12f\xde\xd5\x08\x00H$\x00(\x85\xc2\x11\xcc\x83\x01\xf1\x94\xff\xfc\xbf\x067\x17\xd9\x86\xd4\x96\xbf\xdfdv$a\xae\x01\xd0\x90\n\x07\x1d\xfd\xdb\t3\xad'
ex_complet2 = b'\xb3\x82\x90ze\xe66?HJ#9\x08\x00Hu\x00G\\S\n{\r\x06\x0f\x93\x1f\xc9\xa5\xd0\xac\xea\xbc\xea\xc4\x13a\xdet>\xe1\x13\x9cJ\x8f\x1b\x03\x15\xf5\x83\x00\x00\x11L\x00\x00\r\xea\x80:\\\x9dJ\x9c)\xaf\xba\xcc){\xc0\x97\x83\xc4\xcd\xec3\xb4bravo !'
ex_complet3 = b"\x8e`\x1cV\xbf\x86\xa6\x0b\x8f\x99\xe8\x1e\x08\x00H>\x001\x1e*\xd4\xc5\x13\x11\xb20W'\xce*\xdb+\xc4\xa7\x08}\x99\xfd\xd9\x90\x9d\x1cA/\x1f\x00\x02\x99\xddG\x00\x11\xda\x9asuper ;-)"

def decode_udp(data) :
    """
    Fonction permettant de décoder une trame udp et renvoyant des informations sur l'entête et les données encapsulées.
    Arguments :
        - data : Données au format binaire représentant une trame udp
    Sorties :
        - entete : Chaine de caractères donnant des informations sur l'entête
        - data : Les données encapsulées dans la trame udp
    >>> a = decode_udp(ex_udp)
    >>> len(a) == 2
    True
    >>> a[0] == "        +++ Paquet UDP +++\\n            Port source      : 45\\n            Port destination : 55710\\n            Longueur totale  : 14\\n"
    True
    >>> a[1].decode('utf-8') == "coucou"
    True
    """
    # Décoder les données de l'entête
    data_unpacked = struct.unpack("!HHH",data[0:6])
    # Définir le port source
    source = data_unpacked[0]
    # Définir le port destination
    destination = data_unpacked[1]
    # Définir la longueur
    longueur = data_unpacked[2]
    # Mise en forme de l'entête à renvoyer
    entete = f"        +++ Paquet UDP +++\n            Port source      : {source}\n            Port destination : {destination}\n            Longueur totale  : {longueur}\n"
    return entete,data[8:]

def decode_tcp(data) :
    """
    Fonction permettant de décoder une trame tcp et renvoyant des informations sur l'entête et les données encapsulées.
    Arguments :
        - data : Données au format binaire représentant une trame tcp
    Sorties :
        - entete : Chaine de caractères donnant des informations sur l'entête
        - data : Les données encapsulées dans la trame tcp
    >>> a = decode_tcp(ex_tcp)
    >>> len(a) == 2
    True
    >>> a[0] == "        +++ Paquet TCP +++\\n            Port source      : 45\\n            Port destination : 55131\\n            Longueur en-tête : 8\\n"
    True
    >>> a[1].decode('utf-8') == "coincoin"
    True
    """
    # Décoder les données de l'entête
    data_unpacked = struct.unpack("!HH",data[0:4])
    # Définir le port source
    source = data_unpacked[0]
    # Définir le port destination
    destination = data_unpacked[1]
    # Définir la longueur
    longueur = struct.unpack("!B",data[12:13])[0] >> 4
    # Mise en forme de l entête à renvoyer
    entete = f"        +++ Paquet TCP +++\n            Port source      : {source}\n            Port destination : {destination}\n            Longueur en-tête : {longueur}\n"
    return entete,data[longueur*4:]

def decode_icmp(data) :
    """
    Fonction permettant de décoder une trame icmp et renvoyant des informations sur l'entête.
    Arguments :
        - data : Données au format binaire représentant une trame icmp
    Sorties :
        - entete : Chaine de caractères donnant des informations sur l'entête
    >>> a = decode_icmp(ex_icmp)
    >>> a == "        +++ Paquet ICMP +++\\n            Type             : 5\\n"
    True
    """
    # Décoder les données de l'entête
    data_unpacked = struct.unpack("!B",data[0:1])
    # Définir le type de la trame icmp
    datatype = data_unpacked[0]
    # Mise en forme de l entête à renvoyer
    entete = f"        +++ Paquet ICMP +++\n            Type             : {datatype}\n"
    return entete

def decode_adresse_IP(addr) :
    """
    Fonction permettant de transformer une adresse IPv4 écrite au format décimal au format x.x.x.x où x est un entier entre 0 et 255.
    Arguments :
        - addr : Un entier représentant une adresse IPv4 en décimal
    Sorties :
        - ip_decode : Une chaine de caractères représentant une adresse IPv4 au format x.x.x.x
    >>> decode_adresse_IP(2475088460) == "147.134.218.76"
    True
    """
    # Mise en forme de l'adresse IP
    ip_decode=str((addr>>24)%256)+"."+str((addr>>16)%256)+"."+str((addr>>8)%256)+"."+str(addr%256)
    return ip_decode

def decode_ip(data) :
    """
    Fonction permettant de décoder une trame IP et renvoyant des informations sur l'entête, le protocole encapsulé et les données encapsulées.
    Arguments :
        - data : Données au format binaire représentant une trame IP
    Sorties :
        - entete : Chaine de caractères donnant des informations sur l'entête
        - protocole : Entier représentant le protocole encapsulé dans la trame IP
        - data : Les données encapsulées dans la trame IP
    >>> a = decode_ip(ex_ip)
    >>> len(a) == 3
    True
    >>> a[0] == '    --- Paquet IP ---\\n        Version          : 4\\n        Longueur en-tête : 8\\n        Protocole        : 1\\n        Adresse source   : 234.216.160.229\\n        Adresse dest.    : 76.218.134.147\\n'
    True
    >>> a[1] == 1
    True
    >>> a[2].decode('utf-8') == "cuicui"
    True
    """
    # Décoder les données de l'entête
    data_unpacked = struct.unpack("!B",data[0:1])
    # Définir la version du protocole IP utilisée
    version = data_unpacked[0] >> 4
    # Définir la longueur
    longueur = data_unpacked[0] % 16
    # Définir le protocole encapsulé
    protocole = struct.unpack("!B",data[9:10])[0]
    # Définir le port source
    source = decode_adresse_IP(struct.unpack("!L",data[12:16])[0])
    # Définir le port destination
    destination = decode_adresse_IP(struct.unpack("!L",data[16:20])[0])
    # Mise en forme de l'entête
    entete = f"    --- Paquet IP ---\n        Version          : {version}\n        Longueur en-tête : {longueur}\n        Protocole        : {protocole}\n        Adresse source   : {source}\n        Adresse dest.    : {destination}\n"
    return entete,protocole,data[longueur*4:]


def decode_mac(data) :
    """
    Fonction permettant de transformer une adresse mac de 6 octets encodée en binaire en une adresse de la forme x:x:x:x:x:x où x est un entier en base hexadécimal.
    Arguments :
        - data : Des donnés encodée en binaire représentant une adresse mac
    Sorties :
        - mac : Une chaine de caractère représentant une adresse mac au format x:x:x:x:x:x
    >>> decode_mac(b'R\\x0c\\xc7\\x1d\\xca5') == "52:0c:c7:1d:ca:35"
    True
    """
    # Décoder les données de l'entête
    data_unpack = struct.unpack("!6B", data)
    # Mise en forme de l'adresse mac
    mac = "%.2x" % data_unpack[0]
    for i in range(1,len(data_unpack)):
        nb = "%.2x" % data_unpack[i]
        mac += ":"+str(nb)
    return mac


def decode_Ethernet(data) :
    """
    Fonction permettant de décoder une trame ethernet et renvoyant des informations sur l'entête, le protocole encapsulé et les données encapsulées.
    Arguments :
        - data : Données au format binaire représentant une trame ethernet
    Sorties :
        - entete : Chaine de caractères donnant des informations sur l'entête
        - protocole : Entier représentant le protocole encapsulé dans la trame ethernet
        - data : Les données encapsulées dans la trame ethernet
    >>> a = decode_Ethernet(ex_eth)
    >>> len(a) == 3
    True
    >>> a[0] == '>>> Trame Ethernet <<<\\n    Adresse MAC Destination : 52:0c:c7:1d:ca:35\\n    Adresse MAC Source      : 37:38:1f:55:6b:98\\n    Protocol                : 2048\\n'
    True
    >>> a[1] == 2048
    True
    >>> a[2].decode('utf-8') == "coicoi"
    True
    """
    # Définir l'adresse destination
    destination = decode_mac(data[0:6])
    # Définir l'adresse source
    source = decode_mac(data[6:12])
    # Définir le protocole encapsulé
    protocol = struct.unpack("!H", data[12:14])[0]
    # Mise en forme de l'entête
    entete = f">>> Trame Ethernet <<<\n    Adresse MAC Destination : {destination}\n    Adresse MAC Source      : {source}\n    Protocol                : {protocol}\n"
    return entete,protocol,data[14:]

def decode_trame(data) :
    """
    Fonction permettant de décoder une trame réseau et d'afficher les données encapsulées dans les différents protocoles.
    Arguments :
        - data : Données au format binaire représentant une trame ethernet.
    """
    # Décoder le trame ethernet
    ethernet = decode_Ethernet(data)
    print(ethernet[0])
    # Décoder la trame IP si la version est IPv4
    if ethernet[1]==2048:
        ip = decode_ip(ethernet[2])
        print(ip[0])
        # Décoder la trame icmp
        if ip[1]==1:
            icmp=decode_icmp(ip[2])
            print(icmp)
        # Décoder la trame tcp
        elif ip[1]==6:
            tcp=decode_tcp(ip[2])
            print(tcp[0])
            print(tcp[1])
        # Décoder la trame udp
        elif ip[1]==17:
            udp=decode_udp(ip[2])
            print(udp[0])
            print(udp[1])


if __name__ == "__main__" :
    doctest.testmod()
    print("ex_complet1 :")
    decode_trame(ex_complet1)
    print("ex_complet2 :")
    decode_trame(ex_complet2)
    print("ex_complet3 :")
    decode_trame(ex_complet3)
    # Définir un socket qui écoute les trames ethernet
    ecoute = socket.socket(socket.AF_PACKET,socket.SOCK_RAW,socket.htons(0x0003))
    # Écouter et analyser continuellement les trames
    while True:
        data = ecoute.recvfrom(65565)
        decode_trame(data[0])
