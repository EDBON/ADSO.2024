class Universidad:
    matriculados = 0  

    def __init__(self, nombre):
        self.nombre = nombre
        Universidad.matriculados += 1  

    @classmethod
    def obtener_matriculados(cls):
        return f"Hay {cls.matriculados} estudiantes matriculados"


estudiante1 = Universidad("Juan")
estudiante2 = Universidad("Ana")

print(Universidad.obtener_matriculados()) 
