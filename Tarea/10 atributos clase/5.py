class Coche:
    ruedas = 4  # Atributo de clase compartido por todos los coches

    def __init__(self, marca, precio):
        self.marca = marca
        self.precio = precio

    def info(self):
        return f"Este coche tiene {Coche.ruedas} ruedas y El precio del {self.marca} es ${self.precio}"

coche1 = Coche("Toyota", 20000)
coche2 = Coche("Honda", 22000)

print(coche2.info()) 
