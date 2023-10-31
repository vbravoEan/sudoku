# game/player.py

class Player:
    def __init__(self, name=""):
        self.name = name
        self.score = 0

    def agregar_puntos(self, puntos):
        self.score += puntos