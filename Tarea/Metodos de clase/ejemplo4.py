class Texto:
    @classmethod
    def en_mayusculas(cls, texto):
        return texto.upper()

print(Texto.en_mayusculas("hola mundo"))  # Salida: HOLA MUNDO
