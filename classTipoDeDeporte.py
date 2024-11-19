from classDeporte import Deportes

class Disciplina(Deportes):
    def __init__(self, nombre, minutos_entrenamiento, minutos_juego, minutos_descanso, numero_jugadores, tipo, nivel):
        # Llamada al constructor de la clase base (Deportes) con todos los parámetros
        super().__init__(nombre, minutos_entrenamiento, minutos_juego, minutos_descanso, numero_jugadores, tipo, nivel)


    def get_tipo(self):
        return self._tipo

    def set_tipo(self, tipo):
        self._tipo = tipo

    def get_nivel(self):
        return self._nivel

    def set_nivel(self, nivel):
        self._nivel = nivel
