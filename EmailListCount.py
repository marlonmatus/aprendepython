# 8.5 Open the file mbox-short.txt and read it line by line. When you find a line 
# that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line 
# (i.e. the entire address of the person who sent the message). Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of 
# the sample output to see how to print the count.

# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

fhand=input("Enter file name: ")
fh=open(fhand,'r')
cont=0
for line in fh:
    line=line.rstrip() # Borra los espacios de la derecha
    if not line.startswith('From'): # Valida si la linea comienza con From
        continue
    email=line.split() # Traslada la linea a una lista de palabras
    if len(email)>2: # Define si es una linea de correo enviado
        print(email[1]) # Imprime el correo de la lista
        cont=cont+1 # Hace un conteo de los correos encontrados
    else:continue
print("There were " + str(cont) + " lines in the file with From as the first word")
fh.close()