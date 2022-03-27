tecla1= input("digite la opcion de la tecla 1: ")
tecla2= input("digite la opcion de la tecla 2: ")
if tecla1=="ctrl" and tecla2=="v":
    print("pegar")
elif tecla1=="ctrl" and tecla2=="c": 
    print("copiar")
elif tecla1=="ctrl" and tecla2=="a": 
    print("seleccionar todo el texto")
elif tecla1=="ctrl" and tecla2=="x": 
    print("cortar")
elif tecla1=="ctrl" and tecla2== "n":
    print ("nuevo documento")
else: 
    print("no ejecuta")