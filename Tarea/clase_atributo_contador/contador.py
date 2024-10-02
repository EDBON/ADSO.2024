class Objeto:
    contador_objetos = 0

    def __init__(self):
        Objeto.contador_objetos += 1

    @classmethod
    def total_objetos(cls):
        return f'Se han creado {cls.contador_objetos} objetos.'

# Crear instancias
obj1 = Objeto()
obj2 = Objeto()
obj3 = Objeto()

print(Objeto.total_objetos())  # Salida: Se han creado 3 objetos.
