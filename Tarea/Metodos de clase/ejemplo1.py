class Contador:
    objetos_creados = 0

    def __init__(self):
        Contador.objetos_creados += 1

    @classmethod
    def mostrar_conteo(cls):
        return f'Objetos creados: {cls.objetos_creados}'

# Crear instancias
a = Contador()
b = Contador()

print(Contador.mostrar_conteo())  # Salida: Objetos creados: 2
