# El código establece una conexión a un servidor web, envía una solicitud HTTP 
# para obtener un archivo de texto y luego imprime el contenido del archivo recibido. 
# Finalmente, cierra la conexión.

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


# Estos son los datos solicitados por el curso de Python para todos:
# HTTP/1.1 200 OK
# Date: Mon, 28 Apr 2025 17:49:39 GMT
# Server: Apache/2.4.52 (Ubuntu)
# Last-Modified: Sat, 13 May 2017 11:22:22 GMT
# ETag: "1d3-54f6609240717"
# Accept-Ranges: bytes
# Content-Length: 467
# Cache-Control: max-age=0, no-cache, no-store, must-revalidate
# Pragma: no-cache
# Expires: Wed, 11 Jan 1984 05:00:00 GMT
# Connection: close
# Content-Type: text/plain