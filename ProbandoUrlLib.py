import urllib.request, urllib.parse, urllib.error

fhand=urllib.request.urlopen('http://www.py4inf.com/code/romeo.txt')
for line in fhand:
    line=line.decode().strip()
    print(line) 

fhand=urllib.request.urlopen('http://www.py4inf.com/code/romeo.txt')
count= dict()
for line in fhand:
    words= line.decode().split()
    for word in words:
        count[word]=count.get(word,0)+1
print(count)    

fhand=urllib.request.urlopen('http://aprende.org/')
for line in fhand:
    line=line.decode().strip()
    print(line)