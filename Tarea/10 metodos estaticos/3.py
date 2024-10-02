class Tiempo:
    @staticmethod
    def minutos_a_segundos(minutos):
        return minutos * 60

# Uso
print(Tiempo.minutos_a_segundos(5))  # 300
