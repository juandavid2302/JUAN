class Cuenta:
    """
    numero
    fecha
    apertura
    saldo
    """

#metodo constructor
    def init(self,numero,fecha,apertura,saldo):
        self.numero=numero
        self.fecha=fecha
        self.apertura=apertura
        self.saldo=saldo

#Metodo setter
    def setNumero(self,numero):
        self.numero=numero
    def setFecha(self,fecha):
        self.fecha=fecha
    def setApertura(self,apertura):
        self.apertura=apertura
    def setSaldo(self,saldo):
        self.saldo=saldo

#Metodo getter
    def getNumero(self):
        return self.numero
    def getFecha(self):
        return self.fecha
    def getApertura(self):
        return self.apertura
    def getSaldo(self):
        return self.saldo

#Metodo Retiro
    def Retiro(self):
        while True:
            self.retiro=int(input('Digite el valor a retirar: '))
            if self.retiro>0 and self.retiro<=self.saldo:
                self.saldo-=self.retiro
                return f'Retiro exitoso {self.saldo}'
            else:
                print(f'Cantidad insuficiente saldo disponible {self.saldo}')
                continue

#Metodo Consignar
    def Consignar(self,valor):
        self.saldo+=valor
        return (self,valor)
    """def obtenerInformacion(self):
        info='Informacion de la Cuenta'
        info+='\n numero: '+str(self.getNumero())
        info+='\n fecha: '+str(self.getFecha())
        info+='\n apertura: '+self.getApertura()
        info+='\n saldo: '+str(self.getSaldo())"""

#implementar la herencia, creo la clase cuenta corriente "Hereda de la clase cuenta"
class Cuentacorriente(Cuenta):
    """
    numerochequera
    """

#Metodo constructor de la hija
    def init(self):
        super().init()
        self.numerochequera='17898'
    #metodo getter
    def getNumerochequera(self):
        return self.numerochequera
    #metodo setter
    def setNumerochequera(self,numerochequera):
        self.numerochequera=numerochequera
    # parametros
    #creando objeto
cuent=cuenta.Cuenta()
cuent.setNumero('140142546212')
cuent.setFecha('1/Enero/2021')
cuent.setApertura('Solicito')
cuent.setSaldo('50.000.444')
print(f'la cuenta : {cuent.getNumero()} del {cuent.getFecha()} {cuent.getApertura()} {cuent.getSaldo()} ')
print(cuent.Retiro())
#print(Consignar(','))
print('----------------------------------------------')
print('AQUI EMPIEZA LA SUBCLASE "CUENTA CORRIENTE HIJA DE CUENTA"')
#creando objeto
cuentacorriente=cuenta.Cuentacorriente()
cuentacorriente.setApertura('Aperturo')
cuentacorriente.setFecha('12/Abril/2021')
print(f'la cuenta corriente: {cuentacorriente.getApertura()} {cuentacorriente.getFecha()}')
print(cuentacorriente.setNumerochequera(','))
print('------------------------------------')