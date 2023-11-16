#Clase con Atributos y Metodos
class CuentaBancaria:

     #Constructor que inicializa los atributos de la cuenta
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    #Metodo para depositar dinero en la cuenta
    def depositar(self, monto):
        self.saldo += monto
        print(f"Se depositaron ${monto} \n Nuevo saldo: ${self.saldo}")

    #Metodo para retirar dinero de la cuenta
    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print(f"Se retiraron ${monto} \n Nuevo saldo: ${self.saldo}")
        else:
            print("Fondos insuficientes")

#Crear una instancia de la clase CuentaBancaria
cuenta = CuentaBancaria("Miguel", 1000)
cuenta.depositar(500)
cuenta.retirar(200)

#Herencia- Definir una clase derivada CuentaCorriente que hereda de CuentaBancaria
class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, saldo, sobregiro):
        # Llamada al constructor de la clase base
        super().__init__(titular, saldo)
        self.sobregiro = sobregiro

    def utilizarSobregiro(self, monto):
        if monto <= self.sobregiro:
            self.sobregiro -= monto
            print(f"Se utilizo el sobregiro \n Nuevo sobregiro: ${self.sobregiro}")
        else:
            print("Sobregiro insuficiente")

# Uso de la clase derivada
class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, saldo, sobregiro):
        # Llamada al constructor de la clase base
        super().__init__(titular, saldo)
        self.sobregiro = sobregiro

    def utilizarSobregiro(self, monto):
        if monto <= self.sobregiro:
            self.sobregiro -= monto
            print(f"Se utilizo el sobregiro \n Nuevo sobregiro: ${self.sobregiro}")
        else:
            print("Sobregiro insuficiente")

# Uso de la clase derivada
cuentaCorriente= CuentaCorriente("Maria", 500, 200)
cuentaCorriente.utilizarSobregiro(700)  # Utilizará el sobregiro
cuentaCorriente.utilizarSobregiro(100)  


#Polimorfismo- Definir una clase derivada CajaAhorro que sobrescribe el metodo retirar
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def mostrarInformacion(self):
        print(f"Cuenta de {self.titular} \n Saldo actual: ${self.saldo}")

class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, saldo, sobregiro):
        super().__init__(titular, saldo)
        self.sobregiro = sobregiro

    def realizarOperacion(self, monto):
        if monto > self.saldo + self.sobregiro:
            print("Fondos insuficientes, operacion no realizada.")
        else:
            self.saldo -= monto
            print(f"Se realizo una operacion en la cuenta corriente \n Nuevo saldo: ${self.saldo}")

class CajaAhorro(CuentaBancaria):
    def realizarOperacion(self, monto):
        if monto > self.saldo:
            print("Fondos insuficientes, operacion no realizada.")
        else:
            self.saldo -= monto
            print(f"Se realizo una operacion en la cuenta de ahorro \n Nuevo saldo: ${self.saldo}")

# Funcion que realiza una operacion en cualquier cuenta
def operarCuenta(cuenta, monto):
    cuenta.realizarOperacion(monto)

# Crear instancias de diferentes cuentas
cuentaCorriente = CuentaCorriente("Miguel", 1000, 500)
cuentaAhorro = CajaAhorro("Maria", 800)

# Realizar operaciones en las cuentas sin preocuparse por el tipo especifico
operarCuenta(cuentaCorriente, 700)
operarCuenta(cuentaAhorro, 200)

# Mostrar informacion de las cuentas
cuentaCorriente.mostrarInformacion()
cuentaAhorro.mostrarInformacion()

#def se utiliza para definir metodos (funciones dentro de una clase).
#__init__ Es conocido como el "constructor" de la clase y se utiliza para inicializar los atributos de la instancia.
#self- es una convencion en Python que se utiliza para referirse al objeto actual dentro de una clase