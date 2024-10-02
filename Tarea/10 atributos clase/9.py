class Empleado:
    empleados_creados = 0  

    def __init__(self, nombre, puesto):
        self.nombre = nombre
        self.puesto = puesto
        Empleado.empleados_creados += 1

    def obtener_info(self):
        return f'''Empleado: {self.nombre}, 
Puesto: {self.puesto}'''

    @classmethod
    def total_empleados(cls):
        return f"Total de empleados creados: {cls.empleados_creados}"


empleado1 = Empleado("Luis", "Ingeniero")
empleado2 = Empleado("María", "Contadora")

print(empleado1.obtener_info())  
print(Empleado.total_empleados())  
