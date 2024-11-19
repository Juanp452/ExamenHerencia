from classTipoDeDeporte import Disciplina

class Futbol(Disciplina):
    def __init__(self, nombre, minutos_entrenamiento, minutos_juego, minutos_descanso, numero_jugadores, tipo, nivel, formacion, tipo_balon):
        super().__init__(nombre, minutos_entrenamiento, minutos_juego, minutos_descanso, numero_jugadores, tipo, nivel)
        self._formacion = formacion
        self._tipo_balon = tipo_balon

    # Métodos para formacion
    def get_formacion(self):
        return self._formacion

    def set_formacion(self, formacion):
        self._formacion = formacion

    # Métodos para tipo_balon
    def get_tipo_balon(self):
        return self._tipo_balon

    def set_tipo_balon(self, tipo_balon):
        self._tipo_balon = tipo_balon
