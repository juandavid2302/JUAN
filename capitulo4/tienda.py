compra= float(input("digite el valor total de su compra: "))

if compra <= 50.000:
    print("no aplica descuento")

else:    
    color=input("DIGITE EL COLOR DE LA BALOTA: ")
    if color=="rojo":
        d= compra*1.0
        t= compra-d
        print(f""" ha sacado la balota de color rojo por lo cual le aplica el descuento del (100%),valor de la compra {compra:.3f},
            el valor del descuento {d:.3f}, el valor a pagar {t:.3f}""")
    
    elif color=="verde":
        d= compra*0.5
        t= compra-d
        print(f""" ha sacado la balota de color verde por lo cual le aplica el descuento del (50%),valor de la compra {compra:.3f},
            el valor del descuento {d:.3f}, el valor a pagar {t:.3f}""")
        
    elif color=="blanco":
        d= compra*0.3
        t= compra-d
        print(f""" ha sacado la balota de color blanco por lo cual le aplica el descuento del (30%),valor de la compra {compra:.3f},
            el valor del descuento {d:.3f}, el valor a pagar {t:.3f}""")
        
    elif color=="negro":
        d= compra*0.2
        t= compra-d
        print(f""" ha sacado la balota de color negro por lo cual le aplica el descuento del (20%),valor de la compra {compra:.3f},
            el valor del descuento {d:.3f}, el valor a pagar {t:.3f}""")
        
    elif color=="amarillo":
        d= compra*0.1
        t= compra-d
        print(f""" ha sacado la balota de color amarillo por lo cual le aplica el descuento del (10%),valor de la compra {compra:.3f},
            el valor del descuento {d:.3f}, el valor a pagar {t:.3f}""")