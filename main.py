from classFutbol import Futbol
from classBasquet import Baloncesto
from classCombateTaekwondo import CombateTaekwondo
from classTaekwondo import Taekwondo

def main():
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
    print("Clase Futbol:")
    print(f"Nombre: {futbol.get_nombre()}")
    print(f"Entrenamiento: {futbol.get_minutos_entrenamiento()} minutos")
    print(f"Juego: {futbol.get_minutos_juego()} minutos")
    print(f"Descanso: {futbol.get_minutos_descanso()} minutos")
    print(f"Jugadores: {futbol.get_numero_jugadores()}")
    print(f"Tipo: {futbol.get_tipo()}")
    print(f"Nivel: {futbol.get_nivel()}")
    print(f"Formación: {futbol.get_formacion()}")
    print(f"Tipo de balón: {futbol.get_tipo_balon()}")
    print()

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
    print("Clase Baloncesto:")
    print(f"Nombre: {baloncesto.get_nombre()}")
    print(f"Entrenamiento: {baloncesto.get_minutos_entrenamiento()} minutos")
    print(f"Juego: {baloncesto.get_minutos_juego()} minutos")
    print(f"Descanso: {baloncesto.get_minutos_descanso()} minutos")
    print(f"Jugadores: {baloncesto.get_numero_jugadores()}")
    print(f"Tipo: {baloncesto.get_tipo()}")
    print(f"Nivel: {baloncesto.get_nivel()}")
    print(f"Posiciones: {baloncesto.get_posiciones()}")
    print(f"Altura mínima: {baloncesto.get_altura_minima()} metros")
    print()

    # Instancia de la clase Taekwondo
    taekwondo = Taekwondo(
        nombre="Taekwondo",
        minutos_entrenamiento=90,
        minutos_juego=4,
        minutos_descanso=3,
        numero_jugadores=2,
        tipo="Deporte individual",
        nivel="Avanzado",
        color_cinturon="Negro",
        fecha_obtencion="2023-05-01",
        estilo="Estilo Olímpico"
    )
    print("Clase Taekwondo:")
    print(f"Nombre: {taekwondo.get_nombre()}")
    print(f"Entrenamiento: {taekwondo.get_minutos_entrenamiento()} minutos")
    print(f"Juego: {taekwondo.get_minutos_juego()} minutos")
    print(f"Descanso: {taekwondo.get_minutos_descanso()} minutos")
    print(f"Jugadores: {taekwondo.get_numero_jugadores()}")
    print(f"Tipo: {taekwondo.get_tipo()}")
    print(f"Nivel: {taekwondo.get_nivel()}")
    print(f"Cinturón: {taekwondo.get_color_cinturon()}")
    print(f"Estilo: {taekwondo.get_estilo()}")
    print()

    # Instancia de la clase CombateTaekwondo
    combate = CombateTaekwondo(
        nombre="Combate Taekwondo",
        minutos_entrenamiento=90,
        minutos_juego=1,
        minutos_descanso=1,
        numero_jugadores=2,
        tipo="Deporte individual",
        nivel="Avanzado",
        color_cinturon="Negro",
        fecha_obtencion="2023-05-01",
        estilo="Estilo Olímpico",
        puntuacion_jueces=8.5,
        tecnicas_utilizadas="Patadas y puñetazos"
    )
    print("Clase Combate Taekwondo:")
    print(f"Nombre: {combate.get_nombre()}")
    print(f"Entrenamiento: {combate.get_minutos_entrenamiento()} minutos")
    print(f"Juego: {combate.get_minutos_juego()} minutos")
    print(f"Descanso: {combate.get_minutos_descanso()} minutos")
    print(f"Jugadores: {combate.get_numero_jugadores()}")
    print(f"Tipo: {combate.get_tipo()}")
    print(f"Nivel: {combate.get_nivel()}")
    print(f"Cinturón: {combate.get_color_cinturon()}")
    print(f"Estilo: {combate.get_estilo()}")
    print(f"Puntuación de jueces: {combate.get_puntuacion_jueces()}")
    print(f"Técnicas utilizadas: {combate.get_tecnicas_utilizadas()}")

if __name__ == "__main__":
    main()
