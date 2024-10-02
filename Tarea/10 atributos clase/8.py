class Banco:
    cuentas_abiertas = 0  

    def __init__(self, nombre_cliente):
        self.nombre_cliente = nombre_cliente
        Banco.cuentas_abiertas += 1  

    @classmethod
    def total_cuentas_abiertas(cls):
        return f"Se han abierto {cls.cuentas_abiertas} cuentas en total."


cuenta1 = Banco("Carlos")
cuenta2 = Banco("Lucía")

print(Banco.total_cuentas_abiertas())  
