# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution 
# by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by 
# finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

# Abrimos el archivo
name = input("Enter file name: ")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

# Creamos un diccionario para contar las horas
counts = dict()

# Recorremos línea por línea del archivo
for line in handle:
    if line.startswith("From "):  
        partes = line.split()
        tiempo = partes[5]           # El tiempo está en la posición 5: 09:14:16
        hora = tiempo.split(":")[0] # Solo queremos la hora: 09
        counts[hora] = counts.get(hora, 0) + 1

# Ordenamos por hora
for clave in sorted(counts):
    print(clave, counts[clave])
