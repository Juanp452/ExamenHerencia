from classTaekwondo import Taekwondo

class CombateTaekwondo(Taekwondo):
    def __init__(self, nombre, minutos_entrenamiento, minutos_juego, minutos_descanso, numero_jugadores, tipo, nivel, color_cinturon, fecha_obtencion, estilo, puntuacion_jueces, tecnicas_utilizadas):
        Taekwondo.__init__(self, nombre, minutos_entrenamiento, minutos_juego, minutos_descanso, numero_jugadores, tipo, nivel, color_cinturon, fecha_obtencion, estilo)
        self._puntuacion_jueces = puntuacion_jueces
        self._tecnicas_utilizadas = tecnicas_utilizadas

    def get_puntuacion_jueces(self):
        return self._puntuacion_jueces

    def set_puntuacion_jueces(self, puntuacion_jueces):
        self._puntuacion_jueces = puntuacion_jueces

    def get_tecnicas_utilizadas(self):
        return self._tecnicas_utilizadas

    def set_tecnicas_utilizadas(self, tecnicas_utilizadas):
        self._tecnicas_utilizadas = tecnicas_utilizadas
