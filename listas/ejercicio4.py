listDos=[]
i=0
while i <= 5:
    Uno=int(input("Digite Un Numero De La Lista: "))
    while Uno < 0:
        print("por favor digite numeros postivos")
        break
    listDos.append(Uno)
    i+=1
    for j in listDos:
        if j < 0:     
            listDos.remove(Uno)
print(listDos)