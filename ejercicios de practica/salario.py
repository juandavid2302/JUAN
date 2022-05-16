nombre=str(input("digite su nombre: "))
salario=int(input("digite su salario: "))
dias_laborados=int(input("digite los dias que laboro: "))
sueldo_devengado=salario*dias_laborados/30
auxilio_de_transporte=83140*dias_laborados/30
smmv=1000000
print("nombre empleado:" ,nombre)
print("salario basico:" ,salario)

if salario<=smmv*2:
    print("auxilio de transporte:" ,auxilio_de_transporte)
    print("salario neto a recibir: " ,sueldo_devengado+auxilio_de_transporte)
elif salario>smmv*2:
    print("no tiene subsidio de transporte")
    print("salario neto a recibir:" ,sueldo_devengado)






    
