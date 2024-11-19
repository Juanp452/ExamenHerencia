from classTipoDeDeporte import Disciplina

class Baloncesto(Disciplina):
    def __init__(self, nombre, minutos_entrenamiento, minutos_juego, minutos_descanso, numero_jugadores, tipo, nivel, posiciones, altura_minima):
        super().__init__(nombre, minutos_entrenamiento, minutos_juego, minutos_descanso, numero_jugadores, tipo, nivel)
        self._posiciones = posiciones
        self._altura_minima = altura_minima

    # Métodos para posiciones
    def get_posiciones(self):
        return self._posiciones

    def set_posiciones(self, posiciones):
        self._posiciones = posiciones

    # Métodos para altura_minima
    def get_altura_minima(self):
        return self._altura_minima

    def set_altura_minima(self, altura_minima):
        self._altura_minima = altura_minima
