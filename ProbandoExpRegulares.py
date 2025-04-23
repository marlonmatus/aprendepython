import re

# Busca las lineas que comienzan con From:
fname="mbox-short.txt"
fhand=open(fname,'r')
cont=0
for line in fhand:
    line=line.rstrip()
    if re.search('^From:', line):
        print (line) 
        cont=cont+1

print ("Cantidad de lineas: ", cont)

# Busca la lineas que comienzan con X-

cont=0
for line in fhand:
    line=line.rstrip()
    if re.search('^X.*:', line):
        print (line) 
        cont=cont+1
print ("Cantidad de lineas: ", cont)
fhand.close()

# Utlizar la funcion findall() para extraer cadenas 
x="My favorities 2 numbers are 19 and 42"
y=re.findall('[0-9]+',x)
print(y)
y=re.findall('[AEIOU]+',x)
print(y)

# Coincidencia codiciosa 
x="From: Using the: character"
y=re.findall('F.+:',x) # Coincidencia codiciosa porque busca la ultima coincidencia
print(y)
y=re.findall('F.+?:',x) # Sin coincidencia codiciosa 
print(y)

# Encontrar email y hora 
x="From: marlon.matus@gmail.com Tue Apr 22 20:15:30 2025"
y=re.findall('\S+@\S+',x) # Email 
print(y)
y=re.findall('\S+:\S+',x) # Hora
print(y)
x="From marlon.matus@gmail.com Tue Apr 22 20:15:30 2025"
y=re.findall('^From.(\S+@\S+)',x) # Extracto con parentesis del email
print(y)
x="From marlon.matus@gmail.com Tue Apr 22 20:15:30 2025"
y=re.findall('^From .*@([^ ]*)',x) # Extracto con parentesis del dominio del correo
# tanbien el parametro dentro del parentesis puede ser '@(\S+)' y funciona de la misma manera
print(y)

#Otras formas de busqueda. En este caso estamos buscando valores flotantes en el 
# archivo para todas aquellas lineas que comiencen con X-DSPAM-Confidence
# se trabajara con el archivo mbox-short.txt abierto y encontrar valores flotantes 
fhand=open(fname)
numlist=list()
for line in fhand:
    line=line.rstrip()
    stuff=re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line)
    if len(stuff)!=1:continue
    num=float(stuff[0])
    numlist.append(num)
#print(numlist)
print('Maximum:', max(numlist))
fhand.close()


#Buscando montos en dolares en una expresion
x = "El monto total por su compra es de C$25.00 pagados en efectivo"
y=re.findall('\$([0-9.]+)',x) # buscando el monto por el simbolo de dolar
print(y)

# Fin de la practica