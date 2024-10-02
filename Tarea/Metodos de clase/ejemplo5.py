class Moneda:
    tasa_conversion = 1.2

    @classmethod
    def convertir_a_euros(cls, cantidad):
        return cantidad / cls.tasa_conversion

print(Moneda.convertir_a_euros(120))  # Salida: 100.0
