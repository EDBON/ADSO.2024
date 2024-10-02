class Alumno:
    numero_alumnos = 0

    # Constructor
    def __init__(self, nombre):
        self.nombre = nombre
        Alumno.numero_alumnos += 1  

    @classmethod
    def obtener_total_alumnos(cls):
        print(f'El número de alumnos es: {cls.numero_alumnos}')

    @classmethod
    def pedir_nombres(cls):
        while True:
            nombre = input("Introduce un nombre: ")
            Alumno(nombre)  
            print(f"Hola, {nombre}!")
            
            
            continuar = input("¿Quieres agregar otro nombre? (s/n): ").lower()
            
            if continuar == 'n':
                print("Saliendo del bucle...")
                break

# a1 = Alumno()
# a2 = Alumno()
# a3 = Alumno()

Alumno.pedir_nombres()
Alumno.obtener_total_alumnos()
