from classCinta import Cinta
from classTipoDeDeporte import Disciplina

class Taekwondo(Cinta, Disciplina):
    def __init__(self, nombre, minutos_entrenamiento, minutos_juego, minutos_descanso, numero_jugadores, tipo, nivel, color_cinturon, fecha_obtencion, estilo):
        Cinta.__init__(self, color_cinturon, nivel, fecha_obtencion)
        Disciplina.__init__(self, nombre, minutos_entrenamiento, minutos_juego, minutos_descanso, numero_jugadores, tipo, nivel)
        self._estilo = estilo

    def get_estilo(self):
        return self._estilo

    def set_estilo(self, estilo):
        self._estilo = estilo
