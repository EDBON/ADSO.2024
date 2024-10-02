class Config:
    idioma = "Español"

    @classmethod
    def cambiar_idioma(cls, nuevo_idioma):
        cls.idioma = nuevo_idioma

print(Config.idioma)  # Salida: Español
Config.cambiar_idioma("Inglés")
print(Config.idioma)  # Salida: Inglés
