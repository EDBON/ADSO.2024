class Tienda:
    ventas = 0 

    def __init__(self, producto, precio):
        self.producto = producto
        self.precio = precio
        Tienda.ventas += 1

    def registrar_venta(self):
        return f"Venta registrada: {self.producto} por ${self.precio}"

    @classmethod
    def total_ventas(cls):
        return f"Total de ventas: {cls.ventas}"

# Uso
venta1 = Tienda("Camisa", 20)
venta2 = Tienda("Pantalón", 30)

print(venta1.registrar_venta())  
print(Tienda.total_ventas())  
