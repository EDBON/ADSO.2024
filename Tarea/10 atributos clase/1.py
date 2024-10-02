class Contador:
    total_instancia = 0
    
    def __init__(self):
        Contador.total_instancia +=1 
        
        
    @classmethod
    def obtener_total_instancias(cls):
        return cls.total_instancia

c1 = Contador()
c2 = Contador()
c3 = Contador()
c4 = Contador()

print(f"Total de instancias creadas: {Contador.obtener_total_instancias()}")
    
