# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear 
# in the file. After the dictionary is produced, the program reads through the dictionary using a maximum 
# loop to find the most prolific committer.


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