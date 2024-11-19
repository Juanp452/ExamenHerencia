class Deportes:
    def __init__(self, nombre, minutos_entrenamiento, minutos_juego, minutos_descanso, numero_jugadores, tipo, nivel):
        self._nombre = nombre
        self._minutos_entrenamiento = minutos_entrenamiento
        self._minutos_juego = minutos_juego
        self._minutos_descanso = minutos_descanso
        self._numero_jugadores = numero_jugadores
        self._tipo = tipo
        self._nivel = nivel

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_minutos_entrenamiento(self):
        return self._minutos_entrenamiento

    def set_minutos_entrenamiento(self, minutos_entrenamiento):
        self._minutos_entrenamiento = minutos_entrenamiento

    def get_minutos_juego(self):
        return self._minutos_juego

    def set_minutos_juego(self, minutos_juego):
        self._minutos_juego = minutos_juego

    def get_minutos_descanso(self):
        return self._minutos_descanso

    def set_minutos_descanso(self, minutos_descanso):
        self._minutos_descanso = minutos_descanso

    def get_numero_jugadores(self):
        return self._numero_jugadores

    def set_numero_jugadores(self, numero_jugadores):
        self._numero_jugadores = numero_jugadores

    def get_tipo(self):
        return self._tipo

    def set_tipo(self, tipo):
        self._tipo = tipo

    def get_nivel(self):
        return self._nivel

    def set_nivel(self, nivel):
        self._nivel = nivel
