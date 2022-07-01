def listanueva():
    list=[]
    for i in range(10):
        valor=input("Ingrese Un Elemento:  ")
        list.append(valor)  
    return list

def devolverlista(list):
        print(",".join(map(str,list)))       
def ordenarlista(list):
    print(sorted(list))
   
def revertirlista(list):
    list.sort(reverse=True)
    print(list)

def elemento(list):
    if valor in list:
        list.index(valor)
        print(f':: La Longitud De La Lista es:   :: ',len(list))
#Programa Principal
list=listanueva()
print("El Contenido De La lista es : ", list)    
rango=devolverlista(list)
ordenarlista(list)
revertirlista(list)
valor=input(":: Ingrese Un Elemento:  ::")
print(list.index(valor))
elemento(list)