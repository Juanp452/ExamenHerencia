class Cinta:
    def __init__(self, color_cinturon, nivel, fecha_obtencion):
        self._color_cinturon = color_cinturon
        self._nivel = nivel
        self._fecha_obtencion = fecha_obtencion

    def get_color_cinturon(self):
        return self._color_cinturon

    def set_color_cinturon(self, color_cinturon):
        self._color_cinturon = color_cinturon

    def get_nivel(self):
        return self._nivel

    def set_nivel(self, nivel):
        self._nivel = nivel

    def get_fecha_obtencion(self):
        return self._fecha_obtencion

    def set_fecha_obtencion(self, fecha_obtencion):
        self._fecha_obtencion = fecha_obtencion
