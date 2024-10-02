class Utilidades:
    @staticmethod
    def es_par(numero):
        return numero % 2 == 0

# Uso
numero = 11
print(f"¿El número {numero} es par? {'Sí' if Utilidades.es_par(numero) else 'No'}.")
