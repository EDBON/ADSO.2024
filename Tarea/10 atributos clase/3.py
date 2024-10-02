class Juego:
    dificultad = "Normal" 
    jugadores = []

    def __init__(self, jugador, dificultad):
        self.jugador = jugador
        self.dificultad = dificultad
        Juego.jugadores.append(self)

    @classmethod
    def mostrar_usuarios(cls):
        print("Usuarios ingresados:")
        for jugador in cls.jugadores:
            print(f"Jugador: {jugador.jugador}, Dificultad: {jugador.dificultad}")
        
    @classmethod        
    def pedir_nombre(cls):
        while True:
            nombre = input("Introduce el nombre de usuario: ")
            dificultad = input("Introduce la dificultad que deseas: ")

            # Crear una nueva instancia del juego con el nombre y la dificultad
            Juego(nombre, dificultad)  
            print(f"Hola {nombre} esocgiste la dificultad: {dificultad}!")

            continuar = input("¿Quieres agregar otro usuario? (s/n): ").lower()
            
            if continuar == 'n':
                print("Saliendo...")
                break
    
Juego.pedir_nombre()
Juego.mostrar_usuarios()

# Cambiar la dificultad para todos
# Juego.dificultad = "Difícil"

# jugador1 = Juego("Alice")
# jugador2 = Juego("Bob")

# print(jugador1.dificultad)  # Salida: Difícil
# print(jugador2.dificultad)  # Salida: Difícil
