import socket

# Crear un socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectarse al servidor web
mysock.connect(('data.pr4e.org', 80))

# Preparar y enviar el pedido HTTP
cmd = 'GET /intro-short.txt HTTP/1.0\r\nHost: data.pr4e.org\r\n\r\n'.encode()
mysock.send(cmd)

# Recibir los datos
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

# Cerrar el socket
mysock.close()