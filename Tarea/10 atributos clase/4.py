class Banco:
    balance_total = 10000  # Balance total compartido por todos los clientes

    def __init__(self, nombre):
        self.nombre = nombre
        self.balance = 0

    def depositar(self, cantidad):
        if Banco.balance_total >= cantidad:
            self.balance += cantidad
            Banco.balance_total -= cantidad
        else:
            print("Fondos insuficientes en el banco.")

    @classmethod
    def mostrar_balance_total(cls):
        print(f"Balance total del banco: {cls.balance_total}")

# Crear cuentas de banco
cliente1 = Banco("Carlos")
cliente2 = Banco("Lucía")

# Depositar dinero
cliente1.depositar(5000)
cliente2.depositar(3000)

# Mostrar balance total del banco
Banco.mostrar_balance_total()  # Salida: Balance total del banco: 2000
