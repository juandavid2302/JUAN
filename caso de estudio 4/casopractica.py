clase_ejecutiva = [False]*3
clase_turista = [False]*3

numero_asientos=len(clase_ejecutiva) + len(clase_turista)

def leerMenu():
    print("""Escoja la opcion que va a realizar\n
        a: Reservar asientos del vuelo 
        b: Cancelar reserva""")
    opc=input('Introduzca opcion que desea realizar: ')
    opc = opc.lower()
    return opc

def mostrarAsientos(tipo):
    strTipo = ' disponibles '
    if tipo:
        strTipo = ' no' + strTipo

    print('asientos' + strTipo + 'en clase ejecutiva: ')
    for x in range(len(clase_ejecutiva)):
        if clase_ejecutiva[x] == tipo:
            print(x+1, end=', ' )
    print()
    print('asientos' + strTipo + 'en clase turista: ')
    for x in range(len(clase_turista)):
        if clase_turista[x] == tipo:
            print(x+1+len(clase_ejecutiva), end=', ' )
    print()

def hacer_reservas():
    print('En este momento va ha realizar una reserva')

    reservados = clase_ejecutiva.count(True) + clase_turista.count(True)
        
    if reservados >= numero_asientos:
        print('No tenemos mas asientos para este vuelo')

    if reservados < numero_asientos:
        print('-----------------------------------------')
        mostrarAsientos(False)
        usuario=int(input('Digite el puesto que desea reservar: '))
        ind = usuario -1
        if ind > 5 or ind < 0:
            print('Las sillas del avion van del 1 al 100')
            
        elif ind < len (clase_ejecutiva):
            if not clase_ejecutiva[ind]:
                clase_ejecutiva[ind]=True 
                print('Su Reserva fue exitosa')
                reservados += 1

            else:
                print(f'La silla {usuario} Ya esta reservada')

        else:
            ind -= len(clase_ejecutiva)
            if not clase_turista[ind]:
                clase_turista[ind]=True 
                print('Su Reserva fue exitosa')
                reservados += 1

            else:
                print(f'La silla {usuario} Ya esta reservada')

            print('Se completaron las reservas para este vuelo')
ok=False           
def cancelar_reservados():
    mostrarAsientos(True)
    while not ok:
        try:
            usuario=int(input('Digite el puesto que desea cancelar: '))
            ok=True
            inde = usuario -1
            if inde > 9 or inde < 0:
                print('Las sillas del avion van del 1 al 100')
            

            elif inde < len (clase_ejecutiva):
                if  clase_ejecutiva[inde]:
                clase_ejecutiva[inde]=False 
                print('Su cancelacion fue exitosa')
                    

            else:
                print(f'La silla {usuario} No esta reservada')

        else:
            inde -= len(clase_ejecutiva)
            if  clase_turista[inde]:
                clase_turista[inde]=False
                print('Su cancelacion fue exitosa')
                    

            else:
                print(f'La silla {usuario} No esta reservada')
            

    

#Programa Principal

print()

while True:
    print('--------------------------------')
    opc = leerMenu()
    if opc == 'a':
        hacer_reservas()
    elif opc == 'b':
        cancelar_reservados()
    