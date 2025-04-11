# Abrir archivo
filename=input("Write name of file:")
try:
    handle = open(filename, 'r')
except:
    print(f"No se pudo abrir el archivo")
    quit()

# Diccionario para contar los correos
counts = dict()

# Procesar cada línea
for line in handle:
    line = line.strip()
    # Verificamos si la línea empieza con 'From '
    if line.startswith("From "):
        words = line.split()
        email = words[1]
        counts[email] = counts.get(email, 0) + 1

# Buscar el correo con más mensajes
max_count = None
max_email = None

# Define quien es el mayor sender y cuantos email ha enviado
for email, conta in counts.items():
    if max_count is None or conta > max_count:
        max_count = conta
        max_email = email

print(max_email, max_count)