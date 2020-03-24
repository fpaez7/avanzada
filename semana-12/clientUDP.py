import socket

server_host = socket.gethostbyname("")
server_port = 15000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mensaje = "Hola, simplemente te estoy enviando un mensaje.".encode('ascii')
sock.sendto(mensaje, (server_host, server_port))
