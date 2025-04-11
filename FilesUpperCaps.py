# 7.1 Write a program that prompts for a file name, then opens that file and reads through 
# the file, and print the contents of the file in upper case. Use the file words.txt 
# to produce the output below.
# You can download the sample data at http://www.py4e.com/code3/words.txt

namefile=input("File name:")
file=open(namefile,'r')
  
# Imprimir el texto en mayusculas
for line in file:
    line=line.upper() # Convierte cada linea del archivo en mayusculas 
    print(line.strip()) # Imprime cada linea eliminando saltos de linea

# Cerrar archivo
file.close()    