class Biblioteca:
    libros_prestados = 0  

    def __init__(self, titulo):
        self.titulo = titulo

    def prestar_libro(self):
        Biblioteca.libros_prestados += 1
        return f"Has prestado el libro: {self.titulo}"

    @classmethod
    def obtener_libros_prestados(cls):
        return f"Total de libros prestados: {cls.libros_prestados}"


libro1 = Biblioteca("Cien años de soledad")
libro2 = Biblioteca("Don Quijote")

print(libro1.prestar_libro())  
print(Biblioteca.obtener_libros_prestados())  