class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def crear_anonimo(cls):
        return cls("Anónimo", 0)

# Crear una persona anónima
anonimo = Persona.crear_anonimo()
print(anonimo.nombre)  # Salida: Anónimo
