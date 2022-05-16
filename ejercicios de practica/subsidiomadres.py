edad=int(input("digite la edad: "))
num_hijos=int(input("digite el numero dehijos: "))
if edad>18 and num_hijos<3:
    print("el subsidio es 200.000")
elif edad>18 and num_hijos>=3:
    print("el subsidio es 500.000")
elif edad<18 and num_hijos==1:
    print("el subsidio es 150.000")
else:
    print("no recibe subsidio")
    