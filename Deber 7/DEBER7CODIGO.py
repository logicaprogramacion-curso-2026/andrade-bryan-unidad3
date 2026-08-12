def iniciar_sesion():
    usuario_correcto = "docente"
    contraseña_correcta = "1234"

    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    if usuario == usuario_correcto and contraseña == contraseña_correcta:
        print("\nInicio de sesión exitoso.\n")
        return usuario
    else:
        print("\nUsuario o contraseña incorrectos.")
        return None


def seleccionar_competencia():
    print("Seleccione una competencia digital:")
    print("1. Seguridad digital")
    print("2. Inteligencia Artificial")
    print("3. Comunicación digital")
    print("4. Tecnologías de la Información")
    print("5. Entornos virtuales de aprendizaje")

    opcion = input("Seleccione una opción: ")

    competencias = {
        "1": "Seguridad digital",
        "2": "Inteligencia Artificial",
        "3": "Comunicación digital",
        "4": "Tecnologías de la Información",
        "5": "Entornos virtuales de aprendizaje"
    }

    return competencias.get(opcion, "Competencia no válida")


def seleccionar_evaluacion():
    print("\nSeleccione el tipo de evaluación:")
    print("1. Tema de investigación")
    print("2. Actividad práctica")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        return "Tema de investigación"
    elif opcion == "2":
        return "Actividad práctica"
    else:
        return "Tipo no válido"


# ------------------------------------------
# GENERAR ACTIVIDAD
# ------------------------------------------

def generar_actividad(competencia, tipo_evaluacion):

    if tipo_evaluacion == "Tema de investigación":

        actividad = f"""
Tema de investigación:

Investigue sobre {competencia} y explique su importancia
en el ámbito educativo.

Preguntas orientadoras:
1. ¿Qué es {competencia}?
2. ¿Por qué es importante para los docentes?
3. ¿Cómo puede aplicarse en el aula?
4. Mencione un ejemplo práctico.
"""

    else:

        actividad = f"""
Actividad práctica:

Diseñe una actividad educativa utilizando
la competencia de {competencia}.

Debe incluir:
1. Objetivo de la actividad.
2. Herramientas digitales utilizadas.
3. Procedimiento.
4. Resultado esperado.
"""

    return actividad


# ------------------------------------------
# GENERAR RÚBRICA
# ------------------------------------------

def generar_rubrica():

    rubrica = {
        "conocimiento": 2,
        "aplicacion": 3,
        "argumentacion": 2,
        "ejemplos": 2,
        "redaccion": 1
    }

    return rubrica


# ------------------------------------------
# EVALUAR RESPUESTA
# ------------------------------------------

def evaluar_respuesta(respuesta, rubrica):

    # Simulación de evaluación.
    # Posteriormente aquí se puede conectar una IA.

    puntuacion = 0

    palabras = respuesta.split()

    # Evaluación básica por cantidad de contenido
    if len(palabras) >= 30:
        puntuacion += rubrica["conocimiento"]
    else:
        puntuacion += 1

    if len(palabras) >= 50:
        puntuacion += rubrica["aplicacion"]
    else:
        puntuacion += 1

    if len(palabras) >= 70:
        puntuacion += rubrica["argumentacion"]
    else:
        puntuacion += 1

    if "ejemplo" in respuesta.lower():
        puntuacion += rubrica["ejemplos"]

    if len(respuesta) >= 100:
        puntuacion += rubrica["redaccion"]

    if puntuacion > 10:
        puntuacion = 10

    # Justificación
    if puntuacion >= 8:
        justificacion = (
            "La respuesta demuestra un buen dominio del tema "
            "y presenta información suficiente."
        )

        fortalezas = [
            "Buen desarrollo de la respuesta",
            "Presenta información relevante",
            "Demuestra comprensión del tema"
        ]

        debilidades = [
            "Puede profundizar algunos conceptos"
        ]

        sugerencias = [
            "Agregar ejemplos más específicos",
            "Profundizar la aplicación en el aula"
        ]

    elif puntuacion >= 5:
        justificacion = (
            "La respuesta presenta conocimientos básicos, "
            "pero necesita mayor desarrollo y argumentación."
        )

        fortalezas = [
            "Presenta conocimientos básicos",
            "Responde parcialmente al tema"
        ]

        debilidades = [
            "Falta mayor argumentación",
            "Faltan ejemplos concretos"
        ]

        sugerencias = [
            "Desarrollar más las ideas",
            "Agregar ejemplos prácticos",
            "Explicar mejor la aplicación educativa"
        ]

    else:
        justificacion = (
            "La respuesta necesita mayor desarrollo "
            "y relación con los criterios de evaluación."
        )

        fortalezas = [
            "Existe un intento de responder"
        ]

        debilidades = [
            "Información insuficiente",
            "Poca argumentación",
            "Falta aplicación práctica"
        ]

        sugerencias = [
            "Investigar nuevamente el tema",
            "Desarrollar mejor las ideas",
            "Incluir ejemplos educativos"
        ]

    return {
        "puntuacion": puntuacion,
        "justificacion": justificacion,
        "fortalezas": fortalezas,
        "debilidades": debilidades,
        "sugerencias": sugerencias
    }


# ------------------------------------------
# MOSTRAR RESULTADOS
# ------------------------------------------

def mostrar_resultados(resultado):

    puntuacion = resultado["puntuacion"]

    print("\n")
    print("=" * 50)
    print("              RESULTADOS")
    print("=" * 50)

    print(f"Calificación: {puntuacion}/10")

    if puntuacion >= 7:
        print("Estado: CUMPLE CON LOS CRITERIOS")
    else:
        print("Estado: REQUIERE MEJORA")

    print("\nJustificación:")
    print(resultado["justificacion"])

    print("\nFortalezas:")
    for fortaleza in resultado["fortalezas"]:
        print("-", fortaleza)

    print("\nAspectos por mejorar:")
    for debilidad in resultado["debilidades"]:
        print("-", debilidad)

    print("\nSugerencias:")
    for sugerencia in resultado["sugerencias"]:
        print("-", sugerencia)

    print("=" * 50)


# ------------------------------------------
# GUARDAR EVALUACIÓN
# ------------------------------------------

def guardar_evaluacion(
    usuario,
    competencia,
    actividad,
    respuesta,
    resultado
):

    registro = {
        "usuario": usuario,
        "competencia": competencia,
        "actividad": actividad,
        "respuesta": respuesta,
        "puntuacion": resultado["puntuacion"],
        "justificacion": resultado["justificacion"],
        "sugerencias": resultado["sugerencias"]
    }

    # Por ahora solamente mostramos que se guardó.
    # Después se puede guardar en JSON o MongoDB.

    print("\nEvaluación guardada correctamente.")

    return registro


# ------------------------------------------
# PROGRAMA PRINCIPAL
# ------------------------------------------

def main():

    print("=" * 50)
    print(" APP DE EVALUACIÓN FORMATIVA DOCENTE")
    print("=" * 50)

    usuario = iniciar_sesion()

    if usuario is None:
        return

    continuar = "s"

    while continuar.lower() == "s":

        # Seleccionar competencia
        competencia = seleccionar_competencia()

        if competencia == "Competencia no válida":
            print("Opción incorrecta.")
            continue

        # Seleccionar evaluación
        tipo_evaluacion = seleccionar_evaluacion()

        if tipo_evaluacion == "Tipo no válido":
            print("Opción incorrecta.")
            continue

        # Generar actividad
        actividad = generar_actividad(
            competencia,
            tipo_evaluacion
        )

        print("\n========== ACTIVIDAD ==========")
        print(actividad)

        # Generar rúbrica
        rubrica = generar_rubrica()

        print("\n========== RÚBRICA ==========")
        print("Conocimiento: 2 puntos")
        print("Aplicación: 3 puntos")
        print("Argumentación: 2 puntos")
        print("Ejemplos: 2 puntos")
        print("Redacción: 1 punto")

        # Respuesta del docente
        print("\n========== RESPUESTA ==========")
        respuesta = input(
            "Escriba su respuesta:\n"
        )

        # Evaluar
        resultado = evaluar_respuesta(
            respuesta,
            rubrica
        )

        # Mostrar resultados
        mostrar_resultados(resultado)

        # Guardar
        guardar_evaluacion(
            usuario,
            competencia,
            actividad,
            respuesta,
            resultado
        )

        # Nueva evaluación
        continuar = input(
            "\n¿Desea realizar otra evaluación? (s/n): "
        )

    print("\nGracias por utilizar la aplicación.")
    print("FIN")


# ------------------------------------------
# EJECUTAR PROGRAMA
# ------------------------------------------

if __name__ == "__main__":
    main()