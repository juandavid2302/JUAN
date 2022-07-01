def fibonacci(num):
    lista = [0,1]
    if num==1:
        print('0')
    elif num==2:
        print('[0,','1]')
    else:
        while(len(lista)<num):
            lista.append(0)
        if(num==0 or num==1):
            return 1
        else:
            lista[0]=0
            lista[1]=1
            for i in range(2,num):
                lista[i]=lista[i-1]+lista[i-2]
            print(lista)
fibonacci(50)