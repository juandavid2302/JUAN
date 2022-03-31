asistentes = 0
hombres = 0
mujeres = 0
edades_hombres = 0
edades_mujeres = 0
repetir = 's'
edad = 1
min_edad = 999

while repetir=='s' or repetir=='S':
    genero = 0
    edad = int (input ('Ingresa el valor de edad: '))
    if edad<18:
        print ('No se permiten menores de edad a la fiesta.')    
    else:
        min_edad = min(min_edad,edad)
        asistentes+=1
        print ('Selecciona el valor de genero.')
        print ('\t1.- Mujer')
        print('\t2.- Hombre')
        while genero != 1 and genero != 2:
            genero = int (input (': '))
            if genero != 1 and genero != 2:
                print('Valor incorrecto. Ingresalo nuevamente.')
        if genero==1 and edad>=18:
            mujeres+=1
            edades_mujeres += edad
        if genero==2 and edad>=18:
            hombres+=1
            edades_hombres += edad
    if edad != 0:
        repetir = str(input('Deseas repetir el proceso? (S/N):'))
    else:
        break

print('Personas que asistieron a la fiesta:',hombres+mujeres)
print('Número de hombres:', hombres)
print('Número de mujeres', mujeres)
if hombres > 0:
    print('Edad promedio hombres',edades_hombres/hombres)
if mujeres > 0:
    print('Edad promedio mujeres',edades_mujeres/mujeres)
print('Edad de la persona más joven',min_edad)