class Tortuga:
    def __init__(self):
        self.posicion_x = 0

    def adelante(self, pasos):
        self.posicion_x += pasos
        print(f"Tortuga avanza {pasos} pasos. Posición actual: {self.posicion_x}")

    def abajo(self):
        print("La tortuga baja una línea")

    def reiniciar(self):
        self.posicion_x = 0
        print("La posición fue reiniciada a 0")

