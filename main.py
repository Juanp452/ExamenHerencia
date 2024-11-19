from classDeporte import Deportes
from classTipoDeDeporte import Disciplina
from classCinta import Cinta
from classFutbol import Futbol
from classBasquet import Baloncesto
from classCombateTaekwondo import CombateTaekwondo
from classTaekwondo import Taekwondo

def main():
    # Instancia de la clase Deportes con los parámetros correctos
    deporte = Deportes(
        nombre="Deporte General",
        minutos_entrenamiento=60,
        minutos_juego=90,
        minutos_descanso=15,
        numero_jugadores=11,
        tipo="Deporte de equipo",  # Agregado el tipo
        nivel="Avanzado"  # Agregado el nivel
    )
    print(f"Deporte: {deporte.get_nombre()}, Entrenamiento: {deporte.get_minutos_entrenamiento()} minutos, Juego: {deporte.get_minutos_juego()} minutos")

    # Instancia de la clase Disciplina
    disciplina = Disciplina(
        nombre="Deporte de Equipo",
        minutos_entrenamiento=90,
        minutos_juego=120,
        minutos_descanso=30,
        numero_jugadores=5,
        tipo="Deporte de equipo",
        nivel="Avanzado"
    )
    print(f"Disciplina: {disciplina.get_tipo()}, Nivel: {disciplina.get_nivel()}")

    # Instancia de la clase Futbol
    futbol = Futbol(
        nombre="Fútbol",
        minutos_entrenamiento=120,
        minutos_juego=90,
        minutos_descanso=15,
        numero_jugadores=11,
        tipo="Deporte de equipo",
        nivel="Intermedio",
        formacion="4-3-3",
        tipo_balon="Balón Oficial"
    )
    print(f"Fútbol - Formación: {futbol.get_formacion()}, Tipo de balón: {futbol.get_tipo_balon()}")

    # Instancia de la clase Baloncesto
    baloncesto = Baloncesto(
        nombre="Baloncesto",
        minutos_entrenamiento=100,
        minutos_juego=48,
        minutos_descanso=12,
        numero_jugadores=5,
        tipo="Deporte de equipo",
        nivel="Profesional",
        posiciones=["Base", "Alero", "Pívot"],
        altura_minima=1.90
    )
    print(f"Baloncesto - Posiciones: {baloncesto.get_posiciones()}, Altura mínima: {baloncesto.get_altura_minima()} metros")

    # Instancia de la clase Taekwondo
    taekwondo = Taekwondo(
        nombre="Taekwondo",
        minutos_entrenamiento=90,
        minutos_juego=30,
        minutos_descanso=10,
        numero_jugadores=2,
        tipo="Deporte individual",
        nivel="Avanzado",
        color_cinturon="Negro",
        fecha_obtencion="2023-05-01",
        estilo="Estilo Olímpico"
    )
    print(f"Taekwondo - Cinturón: {taekwondo.get_color_cinturon()}, Estilo: {taekwondo.get_estilo()}")

    # Instancia de la clase CombateTaekwondo
    combate = CombateTaekwondo(
        nombre="Combate Taekwondo",
        minutos_entrenamiento=90,
        minutos_juego=30,
        minutos_descanso=10,
        numero_jugadores=2,
        tipo="Deporte individual",
        nivel="Avanzado",
        color_cinturon="Negro",
        fecha_obtencion="2023-05-01",
        estilo="Estilo Olímpico",
        puntuacion_jueces=8.5,
        tecnicas_utilizadas="Patadas y puñetazos"
    )
    print(f"Combate Taekwondo - Puntuación: {combate.get_puntuacion_jueces()}, Técnicas utilizadas: {combate.get_tecnicas_utilizadas()}")

if __name__ == "__main__":
    main()
