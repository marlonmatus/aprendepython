#Probando los codigos de los videos

#Probando tuplas
x=('Glenn','Sally','Joseph')
print(x[2])

y=(1,9,2)
print(y)
print(max(y))


# Otro ejemplo, puede ser util para crear variables temporales. 
(x,y)=(4,'Fred')
print(y)

(a,b)=(99,98)
print(a) 

#Tuplas y diccionarios
d=dict()
d['swen']=2
d['cwen']=4

for (k,v) in d.items():
    print(k)
    print(v)

tups=d.items()
print(tups)

# Ordenando tuplas 
d={'a':10,'c':21,'b':1}
print(d)
print(sorted(d.items()))

# Ordenando tuplas por valor y no por clave
c={'a':10,'b':1,'c':21}
tmp=list()
for (k,v) in c.items():
    tmp.append((v,k))
print(tmp)
tmp=sorted(tmp,reverse=True)
print(tmp) 


# Probando tuplas abriendo un archivo 

print("Abriendo archivo =========>")
fname="romeo.txt"
fh=open(fname,'r')

counts=dict()
for line in fh:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1

lst=list()
for k,v in counts.items():
    tpl=(v,k)
    lst.append(tpl)
lst=sorted(lst,reverse=True)

for val,key in lst[:10]:
    print(key,val)

