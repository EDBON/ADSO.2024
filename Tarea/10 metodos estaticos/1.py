class ConversorMoneda:
    @staticmethod
    def dolares_a_euros(dolares, tasa_cambio=0.85):
        return dolares * tasa_cambio

# Uso
dolares = 100
print(f"{dolares} dólares son {ConversorMoneda.dolares_a_euros(dolares):.2f} euros.")
